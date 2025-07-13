# VLLM DeepSeek 谷歌 Colab 实验场

一个用于在 Google Colab 中使用 VLLM 运行 DeepSeek 模型的简化实现。这个实验场允许您在 Colab 环境中轻松部署和交互 DeepSeek-R1-Distill-Qwen-1.5B 和其他 DeepSeek 模型。

## 📚 目录

- [VLLM DeepSeek 谷歌 Colab 实验场](#vllm-deepseek-谷歌-colab-实验场)
  - [📚 目录](#-目录)
  - [🚀 特性](#-特性)
  - [🌟 Google Colab 简介](#-google-colab-简介)
    - [什么是 Google Colab？](#什么是-google-colab)
    - [🎯 为什么选择 Google Colab？](#-为什么选择-google-colab)
    - [🔧 支持的硬件规格](#-支持的硬件规格)
  - [📝 Google Colab 注册使用流程](#-google-colab-注册使用流程)
    - [第一步：注册 Google 账户](#第一步注册-google-账户)
    - [第二步：访问 Google Colab](#第二步访问-google-colab)
    - [第三步：创建和配置笔记本](#第三步创建和配置笔记本)
    - [第四步：启用 GPU 加速](#第四步启用-gpu-加速)
    - [第五步：Google Drive 集成（可选）](#第五步google-drive-集成可选)
    - [第六步：基本使用技巧](#第六步基本使用技巧)
    - [第七步：使用限制和注意事项](#第七步使用限制和注意事项)
    - [第八步：升级到付费版本（可选）](#第八步升级到付费版本可选)
  - [📋 前置条件](#-前置条件)
    - [🎯 必需条件](#-必需条件)
    - [🚀 推荐配置](#-推荐配置)
    - [💡 免费资源说明](#-免费资源说明)
  - [🛠️ 快速开始](#️-快速开始)
  - [⚙️ 配置选项](#️-配置选项)
    - [模型参数](#模型参数)
    - [服务器设置](#服务器设置)
  - [🔍 监控和调试](#-监控和调试)
  - [📊 性能提示](#-性能提示)
  - [🚧 故障排除](#-故障排除)
  - [📝 许可证](#-许可证)
  - [🙏 致谢](#-致谢)
  - [🤝 贡献](#-贡献)

## 🚀 特性

- 在 Google Colab 中轻松部署 DeepSeek 模型
- 实时服务器监控和状态检查
- 针对 Colab 的 GPU 环境进行优化
- 模型交互的交互式界面
- 使用 VLLM 进行内存高效的模型服务
- 支持各种 DeepSeek 模型变体

## 🌟 Google Colab 简介

### 什么是 Google Colab？

Google Colab（Colaboratory）是 Google 提供的一个免费的云端 Jupyter 笔记本环境，专门为机器学习和数据科学设计。它最大的优势是**完全免费提供 GPU 和 TPU 资源**，让您无需购买昂贵的硬件就能运行深度学习模型。

### 🎯 为什么选择 Google Colab？

**💰 免费 GPU 资源**
- **Tesla T4 GPU**：15GB 显存，完全免费使用
- **运行时限制**：免费版本每次可连续运行 12 小时
- **每日限制**：通常每天可使用 12-24 小时的 GPU 时间

**🚀 零配置环境**
- 无需安装任何软件，直接在浏览器中运行
- 预装了 TensorFlow、PyTorch、NumPy 等常用库
- 支持 pip 和 apt 包管理器

**☁️ 云端存储**
- 与 Google Drive 无缝集成
- 代码和数据自动保存到云端
- 支持多人协作编辑

**💡 付费升级选项**
- **Colab Pro**：$9.99/月，更长的运行时间和更好的 GPU
- **Colab Pro+**：$49.99/月，包含更强大的 GPU（V100、A100）

### 🔧 支持的硬件规格

| GPU 类型 | 显存 | 免费版本 | 付费版本 | 适用场景 |
|---------|------|----------|----------|----------|
| Tesla T4 | 15GB | ✅ | ✅ | 小型模型训练、推理 |
| Tesla V100 | 16GB | ❌ | ✅ | 中型模型训练 |
| Tesla A100 | 40GB | ❌ | ✅ | 大型模型训练 |
| Tesla L4 | 22.5GB | ❌ | ✅ | 新一代高效推理 |

## 📝 Google Colab 注册使用流程

### 第一步：注册 Google 账户

1. **访问 Google 官网**
   - 打开浏览器，访问 [accounts.google.com](https://accounts.google.com)
   - 点击"创建账户" → "个人用途"

2. **填写注册信息**
   ```
   姓名：输入您的真实姓名
   用户名：选择一个唯一的用户名
   密码：设置强密码（至少8位，包含字母、数字、符号）
   ```

3. **验证手机号码**
   - 输入手机号码接收验证码
   - 输入收到的验证码完成验证

4. **完成账户设置**
   - 添加恢复邮箱（可选但推荐）
   - 同意 Google 服务条款

### 第二步：访问 Google Colab

1. **打开 Colab 官网**
   - 访问 [colab.research.google.com](https://colab.research.google.com)
   - 使用您的 Google 账户登录

2. **初次使用设置**
   - 首次访问会显示欢迎页面
   - 可以选择查看教程或直接开始使用

3. **从 GitHub 打开笔记本**
   ```
   方法一：直接访问 GitHub 链接
   - 在 GitHub 上找到 .ipynb 文件
   - 将 GitHub URL 中的 "github.com" 替换为 "colab.research.google.com/github"
   
   方法二：使用 Colab 打开
   - 在 Colab 中点击"文件" → "打开笔记本"
   - 选择"GitHub"标签页
   - 输入仓库 URL 或搜索用户名/仓库名
   
   方法三：使用徽章链接
   - 点击 README 中的 "Open in Colab" 徽章
   - 自动跳转到 Colab 并加载笔记本
   ```

### 第三步：创建和配置笔记本

1. **创建新笔记本**
   ```
   方法一：点击"新建笔记本"
   方法二：文件 → 新建笔记本
   方法三：使用快捷键 Ctrl+M N
   ```

2. **重命名笔记本**
   - 点击左上角的"Untitled0.ipynb"
   - 输入新名称，如"DeepSeek-VLLM-Demo"

3. **连接到运行时**
   - 点击右上角的"连接"按钮
   - 等待分配计算资源（通常需要10-30秒）

### 第四步：启用 GPU 加速

1. **更改运行时类型**
   ```
   菜单栏 → 代码执行程序 → 更改运行时类型
   或者：Runtime → Change runtime type
   ```

2. **选择硬件加速器**
   ```
   硬件加速器：选择 "GPU"
   GPU 类型：选择 "T4"（免费版本）
   运行时规格：选择 "标准"
   ```

3. **确认设置**
   - 点击"保存"按钮
   - 系统会重新分配带有 GPU 的运行时

4. **验证 GPU 可用性**
   ```python
   # 在代码单元格中运行以下代码
   !nvidia-smi
   
   # 或者使用 Python 检查
   import torch
   print(f"CUDA 可用: {torch.cuda.is_available()}")
   print(f"GPU 数量: {torch.cuda.device_count()}")
   if torch.cuda.is_available():
       print(f"GPU 名称: {torch.cuda.get_device_name(0)}")
   ```

### 第五步：Google Drive 集成（可选）

1. **挂载 Google Drive**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **授权访问**
   - 点击生成的链接
   - 选择您的 Google 账户
   - 点击"允许"授权访问

3. **验证挂载**
   ```python
   import os
   print(os.listdir('/content/drive/MyDrive'))
   ```

### 第六步：基本使用技巧

1. **代码单元格操作**
   ```
   运行当前单元格：Ctrl + Enter
   运行并创建新单元格：Shift + Enter
   添加代码单元格：Ctrl + M B
   添加文本单元格：Ctrl + M M
   删除单元格：Ctrl + M D
   ```

2. **文件上传下载**
   ```python
   # 上传文件
   from google.colab import files
   uploaded = files.upload()
   
   # 下载文件
   files.download('filename.txt')
   ```

3. **安装 Python 包**
   ```python
   # 使用 pip 安装
   !pip install package_name
   
   # 使用 apt 安装系统包
   !apt-get install package_name
   ```

4. **查看系统信息**
   ```python
   # 查看 CPU 信息
   !cat /proc/cpuinfo | grep "model name" | head -1
   
   # 查看内存信息
   !free -h
   
   # 查看磁盘空间
   !df -h
   ```

### 第七步：使用限制和注意事项

1. **免费版本限制**
   ```
   - 连续运行时间：最长 12 小时
   - 空闲超时：90 分钟自动断开
   - 每日使用限制：通常 12-24 小时
   - 存储空间：临时磁盘约 100GB
   ```

2. **最佳实践**
   ```
   - 定期保存工作到 Google Drive
   - 避免长时间空闲（会被自动断开）
   - 大文件建议存储在 Google Drive 中
   - 使用 GPU 时及时释放资源
   ```

3. **常见问题解决**
   ```
   问题：无法连接到 GPU
   解决：重新选择运行时类型，或稍后重试
   
   问题：运行时意外断开
   解决：重新连接运行时，从 Google Drive 恢复数据
   
   问题：安装包失败
   解决：使用 !pip install --upgrade pip 更新 pip
   ```

### 第八步：升级到付费版本（可选）

1. **Colab Pro 订阅**
   - 访问 [colab.research.google.com/signup](https://colab.research.google.com/signup)
   - 选择 Colab Pro ($9.99/月)
   - 享受更长的运行时间和更好的 GPU

2. **Pro+ 高级功能**
   - 访问更强大的 GPU（V100、A100）
   - 更长的运行时间限制
   - 更大的内存容量
   - 后台执行支持

## 📋 前置条件

在运行实验场之前，请确保您具备：

### 🎯 必需条件
- **Google 账户**：用于访问 Google Colab（完全免费）
- **网络连接**：稳定的互联网连接用于模型下载和推理

### 🚀 推荐配置
- **GPU 运行时**：在 Colab 中启用 GPU 加速（Tesla T4 免费提供）
- **Google Drive**：用于保存代码和模型文件（可选）

### 💡 免费资源说明
- **完全免费**：Google Colab 提供的 Tesla T4 GPU（15GB 显存）
- **无需付费**：所有基础功能都可以免费使用
- **即开即用**：无需安装任何软件或配置环境

## 🛠️ 快速开始

1. **在 Colab 中打开**
   
   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/your-repo/blob/main/deepseek_vllm_demo.ipynb)
   
   > 💡 **提示**：点击上方徽章可直接在 Google Colab 中打开预配置的笔记本

2. **安装依赖**
   ```python
   !pip install fastapi nest-asyncio pyngrok uvicorn

   !pip install vllm
   ```

3. **启动服务器**
   ```python
   import subprocess
   model = 'deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B' # 在此处指定您的模型

   
   vllm_process = subprocess.Popen([
       'vllm',
       'serve',
       'deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B',
       '--trust-remote-code',
       '--dtype', 'half',
       '--max-model-len', '16384',
       '--enable-chunked-prefill', 'false',
       '--tensor-parallel-size', '1'
   ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
   ```

4. **监控服务器状态**
   ```python
   # [包含之前实现的监控代码]
   ```

## ⚙️ 配置选项

### 模型参数
- `--dtype`: 设置为 'half' 以获得最佳 Colab 性能
- `--max-model-len`: 最大序列长度（默认：16384）
- `--tensor-parallel-size`: GPU 并行设置
- `--enable-chunked-prefill`: 预填充优化设置

### 服务器设置
- 默认端口：8000
- 健康检查端点：`/health`
- 生成端点：`/generate`

## 🔍 监控和调试

实验场包含内置的监控功能：
- 实时服务器状态检查
- 输出日志记录（stdout/stderr）
- 错误处理和恢复
- 进程管理

## 📊 性能提示

1. **内存管理**
   - 使用 `dtype=half` 进行高效内存使用
   - 根据需要调整 `max-model-len`
   - 监控 Colab GPU 内存使用情况

2. **优化**
   - 尽可能批处理请求
   - 使用适当的温度设置
   - 监控令牌使用情况

## 🚧 故障排除

常见问题和解决方案：

1. **服务器无法启动**
   - 检查 Colab 中的 GPU 可用性
   - 验证 VLLM 安装
   - 检查内存使用情况

2. **响应时间慢**
   - 减少 `max_tokens`
   - 调整批处理大小
   - 检查网络连接

3. **内存不足**
   - 减少模型参数
   - 清除 Colab 运行时
   - 使用 GPU 重启运行时

## 📝 许可证

本项目基于 MIT 许可证 - 详情请参阅 LICENSE 文件。

## 🙏 致谢

- [VLLM 项目](https://github.com/vllm-project/vllm)
- [DeepSeek AI](https://github.com/deepseek-ai)
- Google Colab 团队

## 🤝 贡献

欢迎贡献！请随时提交问题和拉取请求。