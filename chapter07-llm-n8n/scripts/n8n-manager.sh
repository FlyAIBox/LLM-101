#!/bin/bash

# n8n服务管理脚本
# 用于管理n8n Docker容器和ngrok隧道

# 配置变量
CONTAINER_NAME="n8n"
NGROK_PORT="5678"
N8N_PORT="5678"
DOCKER_IMAGE="docker.1ms.run/n8nio/n8n:1.101.1"
NGROK_PID_FILE="/tmp/ngrok.pid"
WEBHOOK_URL_FILE="/tmp/n8n_webhook_url"

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_debug() {
    echo -e "${BLUE}[DEBUG]${NC} $1"
}

# 获取ngrok URL的函数
get_ngrok_url() {
    local max_attempts=30
    local attempt=1
    local url=""

    # 等待ngrok API可用
    log_debug "等待ngrok API可用..."
    while [ $attempt -le $max_attempts ]; do
        if curl -s http://localhost:4040/api/tunnels > /dev/null 2>&1; then
            break
        fi
        sleep 1
        ((attempt++))
    done

    if [ $attempt -gt $max_attempts ]; then
        log_debug "ngrok API超时" >&2
        return 1
    fi

    # 方法1: 使用Python解析JSON
    url=$(curl -s http://localhost:4040/api/tunnels | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    tunnels = data.get('tunnels', [])
    for tunnel in tunnels:
        public_url = tunnel.get('public_url', '')
        if public_url.startswith('https://') and 'ngrok' in public_url:
            print(public_url)
            break
except Exception:
    pass
" 2>/dev/null)

    # 方法2: 备用grep方法
    if [ -z "$url" ]; then
        log_debug "Python方法失败，尝试grep方法" >&2
        url=$(curl -s http://localhost:4040/api/tunnels | grep -o '"public_url":"https://[^"]*"' | head -1 | cut -d'"' -f4)
    fi

    # 验证URL格式
    if [[ "$url" =~ ^https://.*\.ngrok.*\.app$ ]]; then
        log_debug "成功获取URL: $url" >&2
        echo "$url"
        return 0
    else
        log_debug "URL格式验证失败: $url" >&2
        return 1
    fi
}

# 检查依赖
check_dependencies() {
    log_info "检查依赖..."
    
    if ! command -v docker &> /dev/null; then
        log_error "Docker未安装，请先安装Docker"
        exit 1
    fi
    
    if ! command -v ngrok &> /dev/null; then
        log_error "ngrok未安装，请先安装ngrok"
        exit 1
    fi
    
    log_info "依赖检查完成"
}

# 启动ngrok
start_ngrok() {
    log_info "启动ngrok隧道..."

    # 检查ngrok是否已经运行
    if pgrep -f "ngrok http" > /dev/null; then
        log_warn "ngrok已经在运行"

        # 尝试获取已运行ngrok的URL
        log_debug "获取已运行ngrok的URL..."
        WEBHOOK_URL=$(get_ngrok_url)
        if [ $? -eq 0 ] && [ -n "$WEBHOOK_URL" ]; then
            # 清理并保存URL
            CLEAN_URL=$(echo "$WEBHOOK_URL" | grep -o 'https://[^[:space:]]*\.ngrok[^[:space:]]*\.app' | head -1)
            echo $CLEAN_URL > $WEBHOOK_URL_FILE
            log_info "使用已运行的ngrok隧道: $CLEAN_URL"
            return 0
        else
            log_warn "无法获取已运行ngrok的URL，尝试重启ngrok"
            stop_ngrok
        fi
    fi

    # 启动ngrok
    log_debug "启动新的ngrok进程..."
    nohup ngrok http $NGROK_PORT > /tmp/ngrok.log 2>&1 &
    NGROK_PID=$!
    echo $NGROK_PID > $NGROK_PID_FILE

    log_info "等待ngrok启动..."
    sleep 5

    # 获取ngrok URL
    log_debug "获取ngrok URL..."
    WEBHOOK_URL=$(get_ngrok_url)
    if [ $? -ne 0 ] || [ -z "$WEBHOOK_URL" ]; then
        log_error "无法获取ngrok URL"
        return 1
    fi

    # 清理并保存URL
    CLEAN_URL=$(echo "$WEBHOOK_URL" | grep -o 'https://[^[:space:]]*\.ngrok[^[:space:]]*\.app' | head -1)
    echo $CLEAN_URL > $WEBHOOK_URL_FILE
    log_info "ngrok隧道已启动: $CLEAN_URL"
    return 0
}

# 停止ngrok
stop_ngrok() {
    log_info "停止ngrok隧道..."
    
    if [ -f $NGROK_PID_FILE ]; then
        NGROK_PID=$(cat $NGROK_PID_FILE)
        if kill -0 $NGROK_PID 2>/dev/null; then
            kill $NGROK_PID
            log_info "ngrok进程已停止"
        fi
        rm -f $NGROK_PID_FILE
    fi
    
    # 强制杀死所有ngrok进程
    pkill -f "ngrok http" 2>/dev/null || true
    
    # 清理文件
    rm -f $WEBHOOK_URL_FILE
    rm -f /tmp/ngrok.log
    
    log_info "ngrok隧道已停止"
}

# 启动n8n容器
start_n8n() {
    log_info "启动n8n容器..."
    
    # 检查容器是否已存在
    if docker ps -a --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        log_warn "容器 $CONTAINER_NAME 已存在"
        
        # 检查容器状态
        if docker ps --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
            log_warn "容器 $CONTAINER_NAME 已在运行"
            return 0
        else
            log_info "启动现有容器..."
            docker start $CONTAINER_NAME
            return $?
        fi
    fi
    
    # 获取webhook URL
    if [ -f $WEBHOOK_URL_FILE ]; then
        WEBHOOK_URL=$(cat $WEBHOOK_URL_FILE)
        # 清理URL，移除可能的调试信息
        WEBHOOK_URL=$(echo "$WEBHOOK_URL" | grep -o 'https://[^[:space:]]*\.ngrok[^[:space:]]*\.app' | head -1)
    else
        log_error "未找到webhook URL，请先启动ngrok"
        return 1
    fi

    if [ -z "$WEBHOOK_URL" ]; then
        log_error "webhook URL为空或格式不正确"
        return 1
    fi

    log_info "使用Webhook URL: $WEBHOOK_URL"
    
    # 创建并启动新容器
    docker run -d \
        --name $CONTAINER_NAME \
        -p $N8N_PORT:5678 \
        -v n8n_data:/home/node/.n8n \
        -v /home/data/n8n_i18n/dist:/usr/local/lib/node_modules/n8n/node_modules/n8n-editor-ui/dist \
        -e WEBHOOK_URL=$WEBHOOK_URL \
        -e N8N_DEFAULT_LOCALE=zh-CN \
        -e GENERIC_TIMEZONE=Asia/Shanghai \
        -e N8N_SECURE_COOKIE=false \
        -e N8N_RUNNERS_ENABLED=true \
        -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
        $DOCKER_IMAGE
    
    if [ $? -eq 0 ]; then
        log_info "n8n容器启动成功"
        log_info "访问地址: http://localhost:$N8N_PORT"
        log_info "外部访问: $WEBHOOK_URL"
    else
        log_error "n8n容器启动失败"
        return 1
    fi
}

# 停止n8n容器
stop_n8n() {
    log_info "停止n8n容器..."
    
    if docker ps --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        docker stop $CONTAINER_NAME
        log_info "n8n容器已停止"
    else
        log_warn "n8n容器未运行"
    fi
}

# 删除n8n容器
remove_n8n() {
    log_info "删除n8n容器..."
    
    # 先停止容器
    stop_n8n
    
    # 删除容器
    if docker ps -a --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        docker rm $CONTAINER_NAME
        log_info "n8n容器已删除"
    else
        log_warn "n8n容器不存在"
    fi
}

# 查看服务状态
status() {
    log_info "检查服务状态..."
    
    echo "==================== 服务状态 ===================="
    
    # 检查ngrok状态
    if pgrep -f "ngrok http" > /dev/null; then
        echo -e "ngrok状态: ${GREEN}运行中${NC}"

        # 尝试从缓存文件获取URL
        local webhook_url=""
        if [ -f $WEBHOOK_URL_FILE ]; then
            webhook_url=$(cat $WEBHOOK_URL_FILE)
        fi

        # 如果缓存文件不存在或为空，尝试实时获取
        if [ -z "$webhook_url" ]; then
            webhook_url=$(get_ngrok_url 2>/dev/null)
            if [ $? -eq 0 ] && [ -n "$webhook_url" ]; then
                # 清理URL，移除可能的调试信息
                webhook_url=$(echo "$webhook_url" | grep -o 'https://[^[:space:]]*\.ngrok[^[:space:]]*\.app' | head -1)
                echo $webhook_url > $WEBHOOK_URL_FILE
            fi
        fi

        if [ -n "$webhook_url" ]; then
            echo "Webhook URL: $webhook_url"
        else
            echo -e "Webhook URL: ${YELLOW}获取中...${NC}"
        fi
    else
        echo -e "ngrok状态: ${RED}未运行${NC}"
    fi
    
    echo "---------------------------------------------------"
    
    # 检查n8n容器状态
    if docker ps --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        echo -e "n8n容器状态: ${GREEN}运行中${NC}"
        echo "本地访问: http://localhost:$N8N_PORT"
        
        # 显示容器信息
        echo "容器信息:"
        docker ps --filter "name=${CONTAINER_NAME}" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    elif docker ps -a --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
        echo -e "n8n容器状态: ${YELLOW}已停止${NC}"
    else
        echo -e "n8n容器状态: ${RED}不存在${NC}"
    fi
    
    echo "=================================================="
}

# 查看日志
logs() {
    local service=$1
    local lines=${2:-50}
    
    case $service in
        "ngrok")
            log_info "查看ngrok日志 (最近 $lines 行)..."
            if [ -f /tmp/ngrok.log ]; then
                tail -n $lines /tmp/ngrok.log
            else
                log_warn "ngrok日志文件不存在"
            fi
            ;;
        "n8n")
            log_info "查看n8n容器日志 (最近 $lines 行)..."
            if docker ps -a --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
                docker logs --tail $lines $CONTAINER_NAME
            else
                log_warn "n8n容器不存在"
            fi
            ;;
        *)
            log_error "未知的服务: $service"
            echo "可用的服务: ngrok, n8n"
            ;;
    esac
}

# 重启服务
restart() {
    log_info "重启所有服务..."
    stop
    sleep 2
    start
}

# 启动所有服务
start() {
    log_info "启动所有服务..."
    check_dependencies
    
    # 启动ngrok
    if ! start_ngrok; then
        log_error "ngrok启动失败"
        exit 1
    fi
    
    # 等待一下确保ngrok完全启动
    sleep 3
    
    # 启动n8n
    if ! start_n8n; then
        log_error "n8n启动失败"
        stop_ngrok
        exit 1
    fi
    
    log_info "所有服务启动完成"
    status
}

# 停止所有服务
stop() {
    log_info "停止所有服务..."
    stop_n8n
    stop_ngrok
    log_info "所有服务已停止"
}

# 显示帮助信息
help() {
    echo "n8n服务管理脚本"
    echo ""
    echo "用法: $0 [命令] [选项]"
    echo ""
    echo "命令:"
    echo "  start          启动所有服务 (ngrok + n8n)"
    echo "  stop           停止所有服务"
    echo "  restart        重启所有服务"
    echo "  status         查看服务状态"
    echo "  logs <service> [lines]  查看日志 (service: ngrok|n8n, lines: 行数，默认50)"
    echo "  remove         删除n8n容器"
    echo "  help           显示此帮助信息"
    echo ""
    echo "示例:"
    echo "  $0 start                # 启动所有服务"
    echo "  $0 logs n8n 100        # 查看n8n最近100行日志"
    echo "  $0 logs ngrok           # 查看ngrok日志"
    echo ""
}

# 主函数
main() {
    case $1 in
        "start")
            start
            ;;
        "stop")
            stop
            ;;
        "restart")
            restart
            ;;
        "status")
            status
            ;;
        "logs")
            logs $2 $3
            ;;
        "remove")
            remove_n8n
            ;;
        "help"|"-h"|"--help")
            help
            ;;
        "")
            help
            ;;
        *)
            log_error "未知命令: $1"
            help
            exit 1
            ;;
    esac
}

# 执行主函数
main "$@"
