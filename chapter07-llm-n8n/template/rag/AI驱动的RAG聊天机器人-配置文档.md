# AI驱动的RAG聊天机器人配置文档

## 前置要求

### 系统要求
- n8n实例（版本 >= 1.0）
- Node.js环境
- 足够的存储空间用于文档处理
- 稳定的网络连接

### 必需的n8n包
确保安装以下n8n包：
```bash
# LangChain相关包
@n8n/n8n-nodes-langchain

# 基础节点包（通常已预装）
n8n-nodes-base
```

## API服务配置

### 1. Google Drive API配置

#### 步骤1：创建Google Cloud项目
1. 访问 [Google Cloud Console](https://console.cloud.google.com/)

2. 创建新项目或选择现有项目

   ![创建新项目或选择现有项目](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171559238.png)

3. 启用以下API：

   点击`API和服务`，然后`启用API和服务`

   - 搜索`Google Drive API`，点击进入，点击`启用`

     ![Google Drive API](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171603295.png)

   - Google Docs API（如果需要聊天历史功能）

     ![Google Docs API](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171603908.png)

#### 步骤2：创建OAuth2凭据
1. 转到`API和服务`中的`凭据`页面

   ![OAuth2凭据](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171605980.png)

2. 点击"创建凭据" > "OAuth 2.0客户端ID"

3. 选择应用类型为"Web应用"

4. 添加授权重定向URI：
   ```bash
   https://your-n8n-instance.com/rest/oauth2-credential/callback
   
   ## 例如
   #https://de51235527c4.ngrok-free.app/rest/oauth2-credential/callback
   ```

5. 记录客户端ID和客户端密钥

   ![创建OAuth2凭据](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171735600.png)

6. 发布应用

   点击左侧的`目标对象(Audience)`, 发布应用

   ![image-20250717193155911](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171931075.png)

#### 步骤3：在n8n中配置Google Drive 账户凭据
1. 在n8n中创建新的"Google Drive OAuth2 API"凭据
2. 输入客户端ID和客户端密钥
3. 点击`Sign in with Google`, 完成OAuth授权流程
4. 测试连接确保正常工作

![在n8n中创建新的"Google Drive OAuth2 API"凭据](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171734964.png)

![完成OAuth授权流程](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171928028.png)

![授予Google Drive权限](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171929270.png)

![配置成功](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171930569.png)

### 2. Google Gemini API配置

#### 步骤1：获取API密钥
1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的API密钥
3. 记录API密钥（保密存储）

![获取Google Gemini API密钥](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171736389.png)

#### 步骤2：在n8n中配置Google Gemini(PaLM) Api 账户凭据
1. 创建"Google Gemini(PaLM) API"凭据
2. 输入API密钥

![image-20250717173843003](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171738249.png)

### 3. OpenAI API配置

#### 步骤1：获取API密钥
1. 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
2. 创建新的API密钥
3. 确保账户有足够的余额

#### 步骤2：在n8n中配置OpenAi 账户凭据
1. 创建"OpenAi"凭据

2. 输入API密钥

   ![image-20250717174244702](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171742951.png)

### 4. Qdrant向量数据库配置

#### 选项A：本地部署Qdrant
```bash
# 使用Docker部署
docker run -d \
    --name qdrant-server \
    -p 6333:6333 \
    -p 6334:6334 \
    -e TZ="Asia/Shanghai" \
    -e QDRANT__SERVICE__GRPC_PORT="6334" \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    docker.1ms.run/qdrant/qdrant:v1.14.1
```

##### 访问 Web UI

Qdrant 的 Web UI 是您的 Qdrant 集合、REST API 和数据点的直观、高效的图形界面。

> Qdrant 的 Web UI 地址：`ip:6333/dashboard`

![Qdrant 的 Web UI ](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171808894.png)

#### 步骤：在n8n中配置QdrantApi账户凭据
1. 创建"Qdrant API"凭据
2. 输入连接URL（本地：http://localhost:6333，云端：提供的URL）
3. 输入API密钥（如果使用云端服务）

![在n8n中配置QdrantApi账户凭据](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171812015.png)

### 5. Telegram Bot配置（可选）

#### 步骤1：创建Telegram Bot
1. 在Telegram中找到@BotFather
2. 发送 `/newbot` 命令
3. 按提示设置bot名称和用户名
4. 记录bot token

#### 步骤2：获取聊天ID
1. 将bot添加到您的聊天或群组
2. 发送消息给bot
3. 访问：`https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. 从响应中找到chat_id

#### 步骤3：在n8n中配置
1. 创建"Telegram API"凭据
2. 输入bot token
3. 设置环境变量 `TELEGRAM_CHAT_ID`

## 工作流参数配置

### 1. Google Drive文件夹配置

在"Google文件夹ID"节点中：
```json
{
  "folder_id": "your-google-drive-folder-id"
}
```

**获取文件夹ID方法：**

1. 访问[Google Drive](https://drive.google.com/drive/home)在`Google Drive`中新建文件夹

   ![image-20250717181527600](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171815699.png)

2. 在Google Drive中打开目标文件夹

3. 从URL中复制文件夹ID：

   ```bash
   https://drive.google.com/drive/folders/[FOLDER_ID]
   ```

   ![](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171817470.png)

### 2. Qdrant集合配置

在"Qdrant集合名称"节点中：
```json
{
  "qdrant_collection_name": "llm101"
}
```

**集合命名建议：**
- 使用描述性名称
- 避免特殊字符
- 使用小写字母和连字符

![image-20250717183118747](https://cdn.jsdelivr.net/gh/Fly0905/note-picture@main/imag/202507171831055.png)

### 3. 文档处理参数

#### 令牌分割器配置
```json
{
  "chunkSize": 3000,
  "chunkOverlap": 200
}
```

#### 嵌入模型配置
```json
{
  "model": "text-embedding-3-large",
  "dimensions": 3072
}
```

### 4. AI模型参数

#### Gemini模型配置
```json
{
  "modelName": "models/gemini-2.0-flash-exp",
  "temperature": 0.4,
  "maxOutputTokens": 8192
}
```

#### 系统提示配置
可以在"AI代理"节点中自定义系统提示：
```
您是一个专门使用文档回答用户问题的智能助手。
请基于检索到的上下文提供准确、相关的答案。
如果无法在文档中找到答案，请明确说明。
```

## 环境变量配置

在n8n中设置以下环境变量：

```bash
# Telegram配置（可选）
TELEGRAM_CHAT_ID=your-telegram-chat-id

# OpenAI配置（在代码节点中使用）
OPENAI_API_KEY=your-openai-api-key

# Qdrant配置（如果需要）
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=your-qdrant-api-key
```

## 安全配置

### 1. API密钥管理
- 使用n8n的凭据管理系统存储所有API密钥
- 定期轮换API密钥
- 监控API使用情况和成本

### 2. 访问控制
- 限制Google Drive文件夹的访问权限
- 设置适当的n8n工作流权限
- 使用强密码和双因素认证

### 3. 数据保护
- 定期备份Qdrant向量数据
- 加密敏感数据传输
- 遵守数据保护法规（GDPR等）

## 性能优化配置

### 1. 并发处理
```json
{
  "batchSize": 10,
  "maxConcurrency": 3
}
```

### 2. 缓存配置
- 启用n8n执行缓存
- 配置适当的TTL值
- 使用Redis作为缓存后端（推荐）

### 3. 资源限制
```json
{
  "maxExecutionTime": 300,
  "maxMemoryUsage": "1GB"
}
```

## 监控和日志配置

### 1. 日志级别
```bash
# 在n8n配置中设置
N8N_LOG_LEVEL=debug
N8N_LOG_OUTPUT=console,file
```

### 2. 健康检查
- 配置定期健康检查
- 监控API响应时间
- 设置告警阈值

### 3. 指标收集
- 启用n8n指标收集
- 集成Prometheus/Grafana
- 监控工作流执行统计

## 故障排除配置

### 1. 重试配置
```json
{
  "retryOnFail": true,
  "maxRetries": 3,
  "retryInterval": 1000
}
```

### 2. 错误处理
- 配置适当的错误处理节点
- 设置错误通知
- 记录详细的错误日志

### 3. 调试模式
```bash
# 启用调试模式
N8N_DEBUG=true
```

## 部署配置

### 1. 生产环境
- 使用HTTPS连接
- 配置负载均衡
- 设置自动扩缩容

### 2. 备份策略
- 定期备份工作流配置
- 备份向量数据库
- 测试恢复流程

### 3. 更新策略
- 制定版本控制策略
- 测试环境验证
- 渐进式部署

---

*配置完成后，请参考使用文档了解如何操作工作流。*
