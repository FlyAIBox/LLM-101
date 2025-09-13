# 🚀 LLM101: 零基础实战大模型

<div align="center">

![LLM Logo](https://img.shields.io/badge/大模型-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-orange.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**🚀 开始您的大模型之旅吧！**<br/>

[📖 课程内容](#-课程内容) • [🚀 环境搭建](#-环境搭建) • [🎯 实战项目](#-实战项目) 

</div>

---

## 📖 课程内容

本课程采用理论与实践相结合的方式，从零基础开始，逐步深入大模型的各个核心技术领域。每个模块都包含详细的理论讲解和实战练习，确保能够真正掌握大模型开发的核心技能。

### 🎯 课程特色

- **零基础友好**：从环境搭建开始，逐步深入
- **实战导向**：每个模块都有完整的实战项目
- **企业级应用**：涵盖真实的企业应用场景
- **技术前沿**：涵盖最新的大模型技术和工具

### 📚 课程大纲

| 模块 | 章节标题 | 核心技术 | 实战项目 |
|------|----------|----------|----------|
| **模块一** | 大模型实战入门与环境搭建 | Python环境、GPU配置、API调用 | 环境配置与API调用实战 |
| **模块二** | 大模型基础推理与提示词工程 | Prompt Engineering、Function Calling | 从零开始构建高效的提示词 |
| **模块三** | VLLM高性能模型推理与压测 | vLLM部署、性能优化、压测 | 本地模型部署与性能测试 |
| **模块四** | MCP项目实战 | MCP优势、应用场景 | AI 旅行规划 MCP 智能体 |
| **模块五** | RAG项目实战 | RAG架构、向量数据库、RAG集成MCP | 企业文档智能问答系统 |
| **模块六** | Agent项目实战 | LangChain Agents、AutoGen、Ango | AI旅行助手 |
| **模块七** | n8n工作流自动化实战 | 可视化工作流、API集成 | 社交媒体内容审核工作流 |
| **模块八** | 大模型高效微调 | LoRA、Q-LoRA、LlamaFactory | 法律领域模型微调 |

### 🐍 Python基础学习

对于零基础的学习者，我们提供了完整的Python学习材料：

#### 📖 学习资源
- **📚 [Python 3 学习指南](chapter01-llm-env/python-base/01-Learning-Python3.md)** - 详细的学习指南和资源链接
- **📓 [Python 3 交互式教程](chapter01-llm-env/python-base/learning-python3.ipynb)** - Jupyter Notebook格式的完整教程

#### 🎯 学习内容
- **基础语法**: 变量、数据类型、操作符、控制流
- **数据结构**: 列表、字典、元组、集合的使用
- **函数编程**: 函数定义、参数传递、作用域
- **面向对象**: 类、对象、继承、多态
- **异常处理**: try-except、错误处理最佳实践
- **大模型应用**: 专门针对大模型开发的Python技能

#### 🚀 快速开始
```bash
# 启动Jupyter Lab
jupyter lab

# 打开Python学习教程
# 文件路径: chapter01-llm-env/python-base/learning-python3.ipynb
```


### 🛠️ 课程技术栈

#### 🤖 大模型基础

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **模型推理** | VLLM、TGI、Ollama | PyTorch、Transformers、CUDA |
| **API调用** | OpenAI API、DeepSeek API | HTTP Client、异步请求 |
| **提示词工程** | CoT、Self-Reflection、Few-shot | Jinja2、LangChain Templates |

#### 🔍 检索增强生成 (RAG)

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **向量数据库** | 相似度检索、元数据过滤 | ChromaDB、Qdrant、Milvus |
| **嵌入模型** | 文本向量化、多语言支持 | BGE、E5、OpenAI Embeddings |
| **文档处理** | 分块、加载、预处理 | LangChain |
| **检索优化** | 重排序、混合检索 | BM25、Dense Retrieval |

#### 🤖 智能代理 (Agent)

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **单Agent** | ReAct、Plan-and-Execute | LangChain Agents |
| **多Agent协作** | 群聊模式、角色分工 | AutoGen、CrewAI |
| **新一代Agent** | 自主规划、工具调用 | Ango Framework |
| **工具集成** | Function Calling、API调用 | 自定义工具、第三方API |

#### 🔧 工作流自动化

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **可视化编排** | 节点连接、数据流 | n8n、Zapier |
| **触发器** | Webhook、定时任务 | Cron、事件驱动 |
| **集成能力** | API连接、数据转换 | HTTP请求、数据映射 |
| **AI智能体** | 工具调用、对话管理 | LangChain、Gemini |

#### 🎯 模型微调

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **高效微调** | LoRA、Q-LoRA、Adapter | PEFT、Usloth、LlamaFactory |
| **全量微调** | 分布式训练、梯度累积 | DeepSpeed、FSDP |
| **数据处理** | 数据清洗、格式转换 | Datasets、Pandas |
| **模型评估** | 指标计算、A/B测试 | BLEU、Rouge、人工评估 |

#### 🚀 部署运维

| 技术分类 | 核心技术 | 主要工具/框架 |
|----------|----------|---------------|
| **容器化** | Docker、Kubernetes | Docker Compose、K8s |
| **监控日志** | 性能监控、日志分析 | Grafana、ELK Stack |
| **负载均衡** | 高可用、弹性伸缩 | Nginx、云负载均衡 |
| **成本优化** | 模型量化、资源调度 | INT8量化、GPU调度 |

---

## 🚀 环境搭建

### 📖 Ubuntu系统配置手册

在开始环境搭建前，建议先阅读我们提供的详细配置手册：

📚 **[Ubuntu 22.04.4 运维配置手册](chapter01-llm-env/linux_ops/Ubuntu22.04.4-运维配置手册.md)**

该手册面向Linux技术初学者，涵盖了从系统基础配置到开发环境搭建的完整流程，包括：
- 🔧 SSH工具配置和静态IP设置
- 👤 用户权限管理和系统时间同步
- 💾 磁盘管理和DNS配置
- 🔨 Git环境、Docker、Node.js等开发工具安装
- 📊 系统监控与维护最佳实践

### 💻 系统要求

- **操作系统**: Ubuntu 22.04 LTS (推荐)
- **Python**: 3.10.18
- **CPU**: >= 2 C
- **内存**: >= 16GB RAM
- **存储**: >= 100GB 可用空间
- **GPU**: NVIDIA GPU (可选，推荐用于模型微调和推理加速)
- **CUDA**: 12.1 (GPU 环境必需)

### 必要的API Keys
在开始之前，请准备以下API Keys中的至少一个：
- [OpenAI API Key(官方)](https://platform.openai.com/api-keys)
- [OpenAI API Key(国内代理)](https://www.apiyi.com/register/?aff_code=we80)
- [DeepSeek API Key](https://platform.deepseek.com/api-keys)
  
### 配置外网访问

> **适用系统：** Linux  
> **用途：** 确保顺利访问Google、HuggingFace、Docker Hub、GitHub等海外服务

#### 操作步骤

**1. 购买代理服务**
- 注册地址：https://yundong.xn--xhq8sm16c5ls.com/#/register?code=RQKCnEWf
- 选择适合的套餐完成购买

**2. 安装 V2rayA 客户端**
- 官方安装教程：https://v2raya.org/docs/prologue/installation/debian/
- 按照教程完成 V2rayA 的安装和配置

**3. 导入订阅链接**
- 获取订阅链接：https://yundong.xn--xhq8sm16c5ls.com/#/knowledge
- 在 V2rayA 界面中导入订阅

**4. 选择并启动节点**
- 在节点列表中选择延迟较低的节点
- 点击左上角的"启动"按钮激活代理

**5. 配置代理模式**
- 访问 V2rayA 管理界面：http://127.0.0.1:2017/
- 进入 **设置** → **透明代理/系统代理**
- 选择：**"分流规则与规则端口所选模式一致"**

#### 验证配置
```bash
# 测试外网连接
curl -I https://www.google.com
curl -I https://huggingface.co
```

### 方法一：自动化脚本（推荐）

```bash
# 1. Git安装(已安装请忽略)
## 更新包列表
sudo apt update
## 安装 Git 
sudo apt install git -y
## 验证Git是否成功安装
git --version

# 2. Git配置（PUSH需要）
## 配置用户名
git config --global user.name "Your Name"
## 配置用户邮箱
git config --global user.email "your.email@example.com"


# 3. 克隆项目
git clone https://github.com/FlyAIBox/LLM-101.git
cd LLM-101

# 4. 运行自动化配置脚本
chmod +x chapter01-llm-env/setup_llm101_dev.sh
./chapter01-llm-env/setup_llm101_dev.sh

# 5. 激活环境
conda activate llm101
```

### 方法二：手动安装

#### 1. GPU驱动与CUDA配置（可选/微调才会用到）

```bash
# 检查GPU硬件
lspci | grep -i nvidia

# 检查GPU状态（如果已安装驱动）
nvidia-smi

# 安装NVIDIA GPU驱动（Ubuntu 22.04）
sudo apt install -y ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
# 安装完成后需要重启系统
sudo reboot

# 安装CUDA 12.1
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run
sudo sh cuda_12.1.0_530.30.02_linux.run --silent --toolkit --toolkitpath=/usr/local/cuda-12.1 --no-opengl-libs --override

# 设置环境变量
echo 'export PATH="/usr/local/cuda-12.1/bin:$PATH"' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH="/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH"' >> ~/.bashrc
source ~/.bashrc

# 验证CUDA安装
nvcc --version
```

#### 2. Python 3.10.18 安装

```bash
# 添加Python PPA源
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update

# 安装Python 3.10和相关工具
sudo apt install -y \
    python3.10 \
    python3.10-dev \
    python3.10-distutils \
    python3.10-venv \
    python3-pip

# 验证安装
python3.10 --version
```

#### 3. Conda环境管理

```bash
# 安装Miniconda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

# 创建虚拟环境
# 创建一个新的、名为 llm101 的 Conda 虚拟环境，并指定在这个环境中安装 Python 3.10.18 版本。它提供了一个隔离的工作空间，避免项目间的依赖冲突。
conda create -n llm101 python=3.10.18
# 用于激活并进入 llm101 这个虚拟环境。
conda activate llm101
```

#### 4. Jupyter Lab 安装和配置

```bash
# 安装Jupyter Lab
conda install -c conda-forge jupyterlab -y

# 生成配置文件
jupyter lab --generate-config

# 后台启动（替换your_password为您的密码）
nohup jupyter lab --port=8000 --NotebookApp.token='your_password' --notebook-dir=./ &

# 访问地址: http://localhost:8000 或 http://your_server_ip:8000
```

#### 5. Git安装和配置

```bash
# Git安装(已安装请忽略)
## 更新包列表
sudo apt update
## 安装 Git 
sudo apt install git -y
## 验证Git是否成功安装
git --version


# Git配置
## 配置用户名
git config --global user.name "Your Name"
## 配置用户邮箱
git config --global user.email "your.email@example.com"
```

#### 6. 克隆项目
```bash
git clone https://github.com/FlyAIBox/LLM-101.git
cd LLM-101
```

## 🎯 第一个大模型应用

### API调用示例
运行您的第一个大模型应用：
```bash
python chapter01-llm-env/first_llm_app.py
```

### 预期输出

```
🚀 LLM-101: 第一个大模型应用
==================================================
✅ 客户端初始化成功
📡 API地址: https://api.openai.com/v1
🤖 使用模型: gpt-3.5-turbo

🚀 正在调用大模型...

🤖 AI助手回复:
📝 你好！我是一个AI助手，可以帮助你解答问题、提供信息、协助编程、翻译文本、创作内容等多种任务。

📊 使用统计:
🔤 输入tokens: 45
🔤 输出tokens: 28
🔤 总计tokens: 73

🎉 恭喜！您的第一个大模型应用运行成功！
```
---

## 🎯 实战项目

#### 🛫 AI旅行助手 (Ango版)
- **位置**: `chapter05-llm-rag/ango/ai_travel_agent/`
- **技术栈**: Ango Framework、多Agent协作、工具调用
- **功能**: 智能旅行规划、景点推荐、行程优化
- **特色**: 展示新一代Agent框架的强大能力

#### 🏢 智慧园区通行助理 (AutoGen版)
- **位置**: `chapter05-llm-rag/autogen/smart_campus/`
- **技术栈**: AutoGen、多Agent协作、群聊模式
- **功能**: 访客预约、权限查询、多Agent协同
- **特色**: 企业级多Agent系统设计

#### 📚 企业文档智能问答
- **位置**: `chapter04-llm-mcp/enterprise_qa/`
- **技术栈**: RAG、ChromaDB、LangChain、MCP
- **功能**: 文档检索、智能问答、上下文优化
- **特色**: RAG技术在企业场景的完整应用

#### 🤖 N8N AI智能体模板
- **位置**: `chapter07-llm-n8n/template/101/`
- **技术栈**: N8N、LangChain、Gemini、工具调用
- **功能**: 可视化AI智能体构建、多工具集成、对话管理
- **特色**: 零代码构建企业级AI智能体，支持天气查询、新闻获取等

#### ⚖️ 智能法律咨询助手
- **位置**: `chapter08-llm-project/legal_assistant/`
- **技术栈**: 全技术栈融合、企业级架构
- **功能**: 法律条文检索、合同分析、风险评估
- **特色**: 企业级项目的完整实现

### 📋 学习路径建议

1. **基础阶段** (模块一~二): 环境搭建 → API调用 → 提示词工程
2. **进阶阶段** (模块三~六): VLLM部署→ MCP实战 → RAG实战 → Agent开发
3. **高级阶段** (模块七~八): 工作流自动化 → 模型微调
4. **项目阶段** (模块九): 企业级项目设计与部署

### 🚀 N8N AI智能体快速开始

如果您想快速体验AI智能体开发，可以：

1. **导入模板**: 使用 `chapter07-llm-n8n/template/101/` 中的N8N模板
2. **配置API**: 获取Gemini API密钥并配置连接
3. **激活工作流**: 启动智能体并开始对话
4. **自定义扩展**: 添加更多工具和功能

详细步骤请参考：[N8N AI智能体快速入门指南](chapter07-llm-n8n/template/101/quick-start.md)


### 🎓 学习成果

完成本课程后，您将能够：

- ✅ 独立搭建大模型开发环境
- ✅ 设计高效的提示词和工作流
- ✅ 部署高性能的大模型推理服务
- ✅ 构建企业级RAG问答系统
- ✅ 开发复杂的多Agent协作系统
- ✅ 实现模型微调和性能优化
- ✅ 设计和部署企业级AI应用

---

## 📞 获取帮助

- 🐛 **Bug报告**: [GitHub Issues](https://github.com/FlyAIBox/LLM-101/issues)
- 💬 **技术讨论**: [GitHub Discussions](https://github.com/FlyAIBox/LLM-101/discussions)
- 📧 **邮件联系**: fly910905@sina.con
- 🔗 **微信公众号**: 萤火AI百宝箱

## 🙏 致谢

本项目使用了以下开源项目：

<table>
<tr>
<td align="center">
<img src="https://pytorch.org/assets/images/logo-dark.svg" width="60">
<br>PyTorch
</td>

<td align="center">
<img src="https://raw.githubusercontent.com/vllm-project/vllm/main/docs/assets/logos/vllm-logo-text-light.png" width="60">
<br>Vllm
</td>

<td align="center">
<img src="https://raw.githubusercontent.com/langchain-ai/.github/main/profile/logo-dark.svg#gh-light-mode-only" width="70">
<br>Langchain
</td>

<td align="center">
<img src="https://camo.githubusercontent.com/3fd5a9a03ec16da77b97a372a8cea9193dd6f1c30aba8f3f7222c1cf30c7e012/68747470733a2f2f61676e6f2d7075626c69632e73332e75732d656173742d312e616d617a6f6e6177732e636f6d2f6173736574732f6c6f676f2d6c696768742e737667" width="60">
<br>Ango
</td>

<td align="center">
<img src="https://docs.unsloth.ai/~gitbook/image?url=https%3A%2F%2F2815821428-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FHpyELzcNe0topgVLGCZY%252Fsites%252Fsite_mXXTe%252Flogo%252FccLeknrOqRa0v4q9P4Qh%252Funsloth%2520graffitti%2520black%2520text.png%3Falt%3Dmedia%26token%3D34deab0c-35f7-462c-8298-e7d8e2771c89&width=320&dpr=2&quality=100&sign=f8e8ce7a&sv=2" width="60">
<br>Unsloth
</td>

<td align="center">
<img src="https://raw.githubusercontent.com/hiyouga/LLaMA-Factory/main/assets/logo.png" width="60">
<br>LLaMA Factory
</td>
</tr>
</table>

特别感谢所有贡献者和社区成员的支持！

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给个Star支持！⭐**

<a href="https://star-history.com/#FlyAIBox/LLM-101&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=FlyAIBox/LLM-101&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=FlyAIBox/LLM-101&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=FlyAIBox/LLM-101&type=Date" />
  </picture>
</a>

**🔗 更多访问：[大模型实战101](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzkzODUxMTY1Mg==&action=getalbum&album_id=3945699220593803270#wechat_redirect)**

</div>


