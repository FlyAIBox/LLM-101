# n8n服务管理脚本使用说明

## 概述

`n8n-manager.sh` 是一个用于管理n8n Docker容器和ngrok隧道的shell脚本，提供了启动、停止、状态查看、日志查看等功能。

## 功能特性

### 🚀 自动化管理
- 自动启动和管理ngrok隧道
- 自动配置n8n容器的webhook URL
- 智能检测服务状态
- 依赖检查和错误处理

### 🔧 完整的生命周期管理
- 服务启动和停止
- 容器创建和删除
- 日志查看和监控
- 状态检查和报告

### 🌐 网络配置
- 自动获取ngrok公网地址
- 配置n8n的webhook URL
- 支持本地和外部访问

## 使用方法

### 基本命令

```bash
# 启动所有服务（ngrok + n8n）
./n8n-manager.sh start

# 停止所有服务
./n8n-manager.sh stop

# 重启所有服务
./n8n-manager.sh restart

# 查看服务状态
./n8n-manager.sh status

# 查看帮助信息
./n8n-manager.sh help
```

### 日志查看

```bash
# 查看n8n容器日志（最近50行）
./n8n-manager.sh logs n8n

# 查看n8n容器日志（最近100行）
./n8n-manager.sh logs n8n 100

# 查看ngrok日志
./n8n-manager.sh logs ngrok

# 查看ngrok日志（最近200行）
./n8n-manager.sh logs ngrok 200
```

### 容器管理

```bash
# 删除n8n容器（会先停止容器）
./n8n-manager.sh remove
```

## 配置说明

### 脚本配置变量

```bash
CONTAINER_NAME="n8n"              # Docker容器名称
NGROK_PORT="5678"                 # ngrok监听端口
N8N_PORT="5678"                   # n8n服务端口
DOCKER_IMAGE="docker.1ms.run/n8nio/n8n:1.101.1"  # Docker镜像
```

### n8n容器环境变量

- `WEBHOOK_URL`: 自动从ngrok获取的公网地址
- `N8N_DEFAULT_LOCALE=zh-CN`: 设置中文界面
- `GENERIC_TIMEZONE=Asia/Shanghai`: 设置时区
- `N8N_SECURE_COOKIE=false`: 开发环境设置
- `N8N_RUNNERS_ENABLED=true`: 启用运行器
- `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true`: 强制文件权限

### 数据卷挂载

- `n8n_data:/home/node/.n8n`: n8n数据持久化
- `/home/data/n8n_i18n/dist`: 中文界面文件（如果存在）

## 工作流程

### 启动流程

1. **依赖检查**: 检查Docker和ngrok是否安装
2. **启动ngrok**: 创建公网隧道并获取URL
3. **启动n8n**: 使用获取的URL创建Docker容器
4. **状态报告**: 显示服务状态和访问地址

### 停止流程

1. **停止n8n容器**: 优雅停止Docker容器
2. **停止ngrok**: 终止ngrok进程和隧道
3. **清理文件**: 删除临时文件和PID文件

## 状态输出示例

```
==================== 服务状态 ====================
ngrok状态: 运行中
Webhook URL: https://742753a8813c.ngrok-free.app
---------------------------------------------------
n8n容器状态: 运行中
本地访问: http://localhost:5678
容器信息:
NAMES    STATUS          PORTS
n8n      Up 2 minutes    0.0.0.0:5678->5678/tcp
==================================================
```

## 访问地址

### 本地访问
- n8n界面: http://localhost:5678
- ngrok管理界面: http://localhost:4040

### 外部访问
- n8n公网地址: 通过ngrok提供的HTTPS地址访问

## 文件说明

### 临时文件
- `/tmp/ngrok.pid`: ngrok进程ID文件
- `/tmp/n8n_webhook_url`: webhook URL缓存文件
- `/tmp/ngrok.log`: ngrok日志文件

### 数据持久化
- `n8n_data`: Docker数据卷，存储n8n的工作流和配置

## 故障排除

### 常见问题

1. **ngrok启动失败**
   ```bash
   # 检查ngrok是否已安装
   which ngrok
   
   # 检查端口是否被占用
   lsof -i :5678
   ```

2. **Docker容器启动失败**
   ```bash
   # 查看Docker日志
   ./n8n-manager.sh logs n8n
   
   # 检查Docker服务状态
   systemctl status docker
   ```

3. **无法获取ngrok URL**
   ```bash
   # 检查ngrok API
   curl -s http://localhost:4040/api/tunnels
   
   # 查看ngrok日志
   ./n8n-manager.sh logs ngrok
   ```

### 手动清理

```bash
# 强制停止所有相关进程
pkill -f ngrok
docker stop n8n
docker rm n8n

# 清理临时文件
rm -f /tmp/ngrok.pid /tmp/n8n_webhook_url /tmp/ngrok.log
```

## 安全注意事项

### ngrok安全
- ngrok免费版会显示警告页面
- 生产环境建议使用付费版或其他内网穿透方案
- 定期更换ngrok地址

### Docker安全
- 容器以非root用户运行
- 数据卷权限适当设置
- 定期更新Docker镜像

### 网络安全
- 限制访问来源IP
- 使用HTTPS连接
- 配置适当的防火墙规则

## 扩展功能

### 自定义配置
可以修改脚本中的配置变量来适应不同环境：

```bash
# 修改端口
NGROK_PORT="8080"
N8N_PORT="8080"

# 修改Docker镜像
DOCKER_IMAGE="n8nio/n8n:latest"
```

### 添加监控
可以集成到系统监控中：

```bash
# 添加到crontab进行健康检查
*/5 * * * * /path/to/n8n-manager.sh status > /dev/null || /path/to/n8n-manager.sh restart
```

### 日志轮转
配置日志轮转避免日志文件过大：

```bash
# 在脚本中添加日志轮转逻辑
if [ -f /tmp/ngrok.log ] && [ $(stat -f%z /tmp/ngrok.log 2>/dev/null || stat -c%s /tmp/ngrok.log) -gt 10485760 ]; then
    mv /tmp/ngrok.log /tmp/ngrok.log.old
fi
```

## 版本信息

- **脚本版本**: 1.0
- **支持的n8n版本**: 1.101.1
- **支持的系统**: Linux/macOS
- **依赖**: Docker, ngrok, curl

---

*使用过程中如有问题，请查看日志文件或联系技术支持。*
