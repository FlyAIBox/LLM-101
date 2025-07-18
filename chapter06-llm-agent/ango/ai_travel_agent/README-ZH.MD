## 🛫 AI旅行助手

这是一个基于Streamlit的AI驱动的旅行助手应用，使用OpenAI GPT-4o生成个性化的旅行行程。它自动化了研究、规划和组织您梦想假期的过程，让您轻松探索令人兴奋的目的地。

### 功能特点
- 研究和发现令人兴奋的旅行目的地、活动和住宿
- 根据您想要旅行的天数定制您的行程
- 利用GPT-4o的强大功能生成智能和个性化的旅行计划
- 支持两种模式：云端GPT-4o和本地Llama-3.2模型

### 技术架构

#### 系统组件
1. **研究员智能体 (Researcher Agent)**
   - 负责根据用户偏好搜索旅行目的地、活动和住宿信息
   - 使用SerpAPI进行网络搜索
   - 分析搜索结果并返回最相关的信息

2. **规划师智能体 (Planner Agent)**
   - 基于研究结果生成详细的行程计划
   - 确保行程结构良好、信息丰富且具有吸引力
   - 提供平衡的建议，包含事实引用

#### 技术栈
- **前端界面**: Streamlit
- **AI框架**: agno (智能体框架)
- **大语言模型**: 
  - OpenAI GPT-4o (云端版本)
  - Ollama Llama-3.2 (本地版本)
- **搜索引擎**: SerpAPI
- **编程语言**: Python

## 环境要求

### 系统环境
- **操作系统**: Ubuntu 22.04.5 LTS (推荐) 或其他Linux发行版
- **Python版本**: Python 3.10.x (推荐使用 3.10.18)
- **包管理器**: conda (推荐) 或 pip

### 硬件要求
- **内存**: 最小4GB RAM，推荐8GB以上
- **存储**: 至少2GB可用空间
- **网络**: 稳定的互联网连接（用于API调用）

## 详细安装和部署指南

### 第一步：环境准备

#### 1. 创建conda虚拟环境
```bash
# 创建Python 3.10虚拟环境
conda create -n ai-travel-agent python=3.10

# 激活虚拟环境
conda activate ai-travel-agent

# 验证Python版本
python --version  # 应该显示 Python 3.10.x
```

#### 2. 克隆项目仓库
```bash
## 【FIXME: 其他仓库记得修改GitHub仓库和项目目录】
# 克隆GitHub仓库
git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git

# 进入项目目录
cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
```

### 第二步：安装依赖包

#### 核心依赖包及其作用说明

```bash
# 安装所有依赖包
pip install -r requirements.txt
```

**依赖包详细说明：**

1. **streamlit** (≥1.46.0)
   - **作用**: 现代化的Python Web应用框架
   - **使用场景**: 构建交互式的用户界面，提供输入框、按钮、显示区域等组件
   - **为什么选择**: 无需前端开发经验即可快速构建美观的Web应用

2. **agno** (≥1.2.8)
   - **作用**: 轻量级的AI智能体框架
   - **使用场景**: 创建和管理AI智能体，支持多种LLM模型和工具集成
   - **为什么选择**: 专为构建智能体应用设计，支持角色定义、工具使用和智能体协作

3. **openai** (≥1.51.0)
   - **作用**: OpenAI官方Python SDK
   - **使用场景**: 与OpenAI的GPT-4o等模型进行API通信
   - **为什么选择**: 官方支持，功能完整，支持流式响应和函数调用

4. **google-search-results** (≥2.4.2)
   - **作用**: SerpAPI的Python客户端库
   - **使用场景**: 执行Google搜索并获取结构化的搜索结果
   - **为什么选择**: 提供可靠的搜索API服务，避免直接爬取搜索引擎的复杂性

#### 验证安装
```bash
# 验证关键包是否正确安装
python -c "import streamlit; print('Streamlit版本:', streamlit.__version__)"
python -c "import agno; print('Agno安装成功')"
python -c "import openai; print('OpenAI版本:', openai.__version__)"
python -c "from serpapi import GoogleSearch; print('SerpAPI安装成功')"
```

### 第三步：配置API密钥

#### 1. 获取OpenAI API密钥
##### 方式一
- 访问 [OpenAI平台](https://platform.openai.com/)
- 注册账户并创建API密钥
- 复制您的API密钥（格式：sk-...）

##### 方式二
- 访问 [OpenAI 国内代理平台](https://www.apiyi.com/register/?aff_code=we80)
- 注册账户并创建API密钥
- 复制您的API密钥（格式：sk-...）
- 修改API地址
```bash
# 在大多数情况下，OpenAI官方库或者一些常用的第三方库会优先识别并使用 OPENAI_API_BASE 或 OPENAI_BASE_URL 作为其 API 地址。
./set_bashrc_env.sh OPENAI_API_BASE "https://vip.apiyi.com/v1"
./set_bashrc_env.sh OPENAI_BASE_URL "https://vip.apiyi.com/v1"
```

#### 2. 获取SerpAPI密钥
- 访问 [SerpAPI官网](https://serpapi.com/)
- 注册账户并获取API密钥(免费用户，100/每月调用次数)
- 复制您的API密钥

#### 3. 配置本地密钥文件
```bash
# 创建Streamlit配置目录
mkdir -p .streamlit

# 创建密钥配置文件
cat > .streamlit/secrets.toml << EOF
# OpenAI API配置
OPENAI_API_KEY = "your-openai-api-key-here"

# SerpAPI配置
SERPAPI_KEY = "your-serpapi-key-here"
EOF
```

**重要提醒**: 
- 将 `your-openai-api-key-here` 替换为您的实际OpenAI API密钥
- 将 `your-serpapi-key-here` 替换为您的实际SerpAPI密钥
- 确保将 `.streamlit/secrets.toml` 添加到 `.gitignore` 文件中

### 第四步：本地运行和测试

#### 1. 启动云端版本（推荐）
```bash
# 确保在项目目录中
cd /path/to/awesome-llm-apps/starter_ai_agents/ai_travel_agent

# 启动Streamlit应用
streamlit run travel_agent.py

# 应用将在浏览器中自动打开，默认地址：http://localhost:8501
```

#### 2. 启动本地版本（需要Ollama）
```bash
# 首先安装Ollama（如果还没有安装）
curl -fsSL https://ollama.ai/install.sh | sh

# 拉取Llama-3.2模型
ollama pull llama3.2

# 启动本地版本
streamlit run local_travel_agent.py
```

#### 3. 测试应用功能
1. 在浏览器中打开应用
2. 输入API密钥（如果使用云端版本）
3. 输入目的地：例如"东京"
4. 选择旅行天数：例如"7天"
5. 点击"生成行程"按钮
6. 等待AI生成个性化的旅行计划

### 第五步：部署到生产环境

#### 1. 部署到Streamlit Community Cloud

**准备工作：**
```bash
# 确保代码已推送到GitHub
git add .
git commit -m "Add AI travel agent application"
git push origin main
```

**部署步骤：**
1. 访问 [Streamlit Community Cloud](https://streamlit.io/cloud)
2. 使用GitHub账户登录
3. 点击"New app"
4. 选择您的GitHub仓库和分支
5. 设置应用路径：`starter_ai_agents/ai_travel_agent/travel_agent.py`
6. 在"Advanced settings"中配置密钥：
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   SERPAPI_KEY = "your-serpapi-key"
   ```
7. 点击"Deploy"

#### 2. 使用Docker部署

**创建Dockerfile：**
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "travel_agent.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**构建和运行：**
```bash
# 构建Docker镜像
docker build -t ai-travel-agent .

# 运行容器
docker run -p 8501:8501 \
  -e OPENAI_API_KEY="your-openai-api-key" \
  -e SERPAPI_KEY="your-serpapi-key" \
  ai-travel-agent
```

### 第六步：性能优化和监控

#### 1. 应用性能优化
```python
# 在应用中添加缓存装饰器
import streamlit as st

@st.cache_data(ttl=3600)  # 缓存1小时
def cached_search_results(query, location):
    # 缓存搜索结果以减少API调用
    pass

@st.cache_resource
def load_model():
    # 缓存模型加载
    pass
```

#### 2. 监控和日志
```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 在关键位置添加日志
logger = logging.getLogger(__name__)
logger.info("Application started")
```

### 文件结构说明

```
ai_travel_agent/
├── README-ZH.MD              # 中文版说明文档（本文件）
├── README.MD                 # 英文版说明文档
├── travel_agent.py           # 主应用（使用OpenAI GPT-4o）
├── local_travel_agent.py     # 本地版本（使用Llama-3.2）
├── requirements.txt          # 项目依赖包列表
├── .streamlit/               # Streamlit配置目录
│   ├── config.toml          # 应用配置文件
│   └── secrets.toml         # API密钥配置（需要手动创建）
├── .gitignore               # Git忽略文件配置
└── assets/                  # 静态资源文件（可选）
    └── images/              # 图片资源
```

### 使用步骤

1. **启动应用**: 运行相应的Python文件
2. **输入API密钥**: 
   - 云端版本：需要OpenAI API密钥和SerpAPI密钥
   - 本地版本：只需要SerpAPI密钥
3. **输入旅行信息**:
   - 目的地：您想去的地方（支持中英文）
   - 旅行天数：1-30天
4. **生成行程**: 点击"生成行程"按钮
5. **查看结果**: 系统将显示个性化的旅行行程

### 特色功能

- **智能搜索**: 自动生成相关的搜索关键词
- **个性化推荐**: 基于目的地和旅行天数定制建议
- **实时搜索**: 使用SerpAPI获取最新的旅行信息
- **结构化输出**: 生成格式良好的行程计划
- **多模型支持**: 支持云端和本地AI模型
- **响应式设计**: 适配不同设备和屏幕尺寸

### 故障排除

#### 常见问题解决方案

1. **API密钥错误**
   ```bash
   # 检查密钥格式
   echo $OPENAI_API_KEY  # 应该以 sk- 开头
   echo $SERPAPI_KEY     # 应该是32位字符串
   ```

2. **依赖包安装失败**
   ```bash
   # 升级pip
   pip install --upgrade pip
   
   # 清理缓存并重新安装
   pip cache purge
   pip install -r requirements.txt --force-reinstall
   ```

3. **端口占用问题**
   ```bash
   # 查找占用端口的进程
   lsof -i :8501
   
   # 使用不同端口启动
   streamlit run travel_agent.py --server.port=8502
   ```

4. **模型加载缓慢**
   ```bash
   # 检查网络连接
   ping api.openai.com
   
   # 使用代理（如果需要）
   export HTTP_PROXY=http://your-proxy:port
   export HTTPS_PROXY=http://your-proxy:port
   ```

### 扩展建议

1. **添加更多搜索源**: 集成更多的旅行信息API
2. **用户偏好存储**: 保存用户的旅行偏好和历史记录
3. **多语言支持**: 支持更多语言的行程生成
4. **导出功能**: 支持将行程导出为PDF或其他格式
5. **图片集成**: 为推荐的景点和活动添加图片
6. **价格比较**: 集成酒店和机票价格比较功能
7. **天气信息**: 添加目的地天气预报
8. **地图集成**: 显示推荐地点的地图位置

### 安全和隐私

- **API密钥安全**: 使用环境变量或密钥管理服务
- **数据隐私**: 不存储用户的个人旅行信息
- **网络安全**: 使用HTTPS进行所有API通信
- **访问控制**: 在生产环境中配置适当的访问控制

### 贡献指南

欢迎贡献代码和建议！请遵循以下步骤：

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

### 许可证

本项目采用MIT许可证。详情请参阅 [LICENSE](LICENSE) 文件。

### 联系方式

如有问题或建议，请通过以下方式联系：
- 创建GitHub Issue
- 发送邮件至项目维护者
- 参与项目讨论区

---

**注意**: 确保您有稳定的网络连接以访问API服务，并且OpenAI API和SerpAPI都需要有效的API密钥。生成的行程质量取决于搜索结果的质量和AI模型的性能。

通过这个AI旅行助手，您可以轻松规划您的下一次旅行，让AI为您处理繁琐的研究和规划工作！🌍✈️ 