# 🛫 AI旅行规划系统 - 基于RAG和CAG技术的智能旅行助手

## 📖 项目概述

本项目实现了一个基于大语言模型和向量检索技术的智能旅行规划系统。系统结合了**检索增强生成(RAG)**和**缓存增强生成(CAG)**技术，能够根据用户偏好生成个性化的旅行计划。

### 🎯 核心功能

- **智能行程规划**: 基于用户偏好生成详细的旅行计划
- **个性化推荐**: 使用向量相似度搜索推荐相关景点和活动
- **预算管理**: 智能分配预算，提供成本估算
- **多模态信息整合**: 整合景点、餐厅、交通等多维度信息
- **实时响应**: 缓存机制确保快速响应

## 🏗️ 技术架构

### 核心技术栈

| 技术组件 | 作用 | 技术特点 |
|---------|------|----------|
| **OpenAI GPT-4** | 生成自然语言旅行计划 | 强大的语言理解和生成能力 |
| **OpenAI Embedding** | 文本向量化 | 1536维向量，捕捉语义信息 |
| **Faiss** | 向量相似度搜索 | 高效的相似度计算和检索 |
| **CAG技术** | 缓存增强生成 | 减少延迟，提高响应速度 |

### 系统架构图

```
用户输入 → 向量化 → Faiss检索 → 知识整合 → GPT-4生成 → 结果展示
    ↓         ↓         ↓         ↓         ↓         ↓
用户偏好   文本向量   相似内容   结构化知识   旅行计划   格式化输出
```

## 🔧 技术原理详解

### 1. 向量化技术 (Embedding)

```python
def get_embedding(text, model="text-embedding-ada-002"):
    """
    将文本转换为数值向量，捕捉语义信息
    - 输入: 自然语言文本
    - 输出: 1536维向量
    - 原理: 相似含义的文本产生相似向量
    """
```

**技术优势:**
- 语义理解: 捕捉文本的深层语义信息
- 相似度计算: 支持高效的相似度搜索
- 多语言支持: 适用于不同语言的文本

### 2. 向量数据库 (Faiss)

```python
# 初始化Faiss索引
self.index = faiss.IndexFlatL2(embedding_dim)

# 添加向量到索引
self.index.add(np.array(self.knowledge_embeddings))

# 相似度搜索
D, I = self.index.search(np.array([query_embedding]), k=5)
```

**技术特点:**
- **高效检索**: 支持大规模向量的快速搜索
- **L2距离**: 使用欧几里得距离计算相似度
- **可扩展性**: 支持动态添加新的向量数据

### 3. 缓存增强生成 (CAG)

```python
# 将相关知识直接嵌入到GPT-4上下文中
relevant_knowledge = self.retrieve_knowledge(preferences)
system_prompt = f"""
    Here's some relevant information about NYC: 
    {self.summarize_knowledge(relevant_knowledge)}
"""
```

**技术优势:**
- **减少延迟**: 避免实时检索外部知识库
- **简化架构**: 降低系统复杂度
- **提高效率**: 预加载相关信息到上下文

### 4. 智能代理架构

```python
class Agent:
    def __init__(self, name, cache_size, embedding_dim=1536):
        # 初始化代理组件
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.embedding_cache = {}
    
    def load_knowledge(self, knowledge_data):
        # 加载知识库
    
    def retrieve_knowledge(self, query):
        # 检索相关知识
    
    def plan_nyc_trip(self, travel_dates, budget, preferences, interests):
        # 生成旅行计划
```

## 📊 知识库结构

### JSON格式设计

```json
{
  "attractions": {
    "Empire State Building": {
      "description": "Iconic skyscraper with observation decks",
      "address": "350 Fifth Avenue, Manhattan",
      "website": "www.esbnyc.com",
      "tips": [
        "Purchase tickets online in advance",
        "Visit during day and night for different views"
      ]
    }
  }
}
```

### 知识库特点

- **结构化存储**: 按类别组织信息
- **详细信息**: 包含描述、地址、网站、提示等
- **可扩展性**: 易于添加新的景点和信息
- **多维度信息**: 涵盖景点、餐厅、交通等多个方面

## 🚀 使用指南

### 环境准备

```bash
# 安装依赖包
pip install openai faiss-cpu tiktoken numpy

# 设置API密钥
export OPENAI_API_KEY="your_api_key_here"
```

### 基本使用

```python
# 创建AI代理
agent = Agent("NYCAI", cache_size=1000)

# 加载知识库
agent.load_knowledge(nyc_knowledge)

# 设置旅行参数
travel_dates = ["2024-04-10", "2024-04-15"]
budget = "$10000"
preferences = "I prefer cultural experiences and local food"
interests = ["museums", "Broadway shows", "Central Park"]

# 生成旅行计划
agent.plan_nyc_trip(travel_dates, budget, preferences, interests)
```

### 输出示例

```
🚀 AI旅行规划系统启动
==================================================
🤖 初始化AI旅行代理...
📚 加载纽约旅行知识库...
📅 旅行日期: 2024-04-10 到 2024-04-15
💰 预算: $10000
🎯 偏好: I prefer cultural experiences and local food
❤️ 兴趣: museums, Broadway shows, Central Park
==================================================

**Transportation:**
* Air Canada Flight 7642 from Montreal to New York City (Estimated Cost: $400)

**Accommodation:**
* The Plaza Hotel, Fifth Avenue (Estimated Cost per night: $700)

**Day 1:**
* **Morning:** Empire State Building (Estimated Cost: $45)
* **Afternoon:** Eleven Madison Park (Estimated Cost: $315)
* **Evening:** Broadway Show (Estimated Cost: $150)
* **Dinner:** The Grill (Estimated Cost per person: $200)

**Total Estimated Cost:** $9881
**Remaining Budget:** $119
**Budget Utilization:** 9881/10000
```

## 🔍 技术亮点分析

### 1. 个性化推荐算法

```python
def retrieve_knowledge(self, query):
    # 1. 查询向量化
    query_embedding = get_embedding(query)
    
    # 2. 相似度搜索
    D, I = self.index.search(np.array([query_embedding]), k=5)
    
    # 3. 返回相关结果
    relevant_info = [self.knowledge_data[i] for i in I[0]]
    return relevant_info
```

**算法优势:**
- 基于语义相似度而非关键词匹配
- 支持模糊查询和同义词理解
- 实时个性化推荐

### 2. 智能预算分配

```python
# 系统提示词中的预算控制
"""
It's crucial that you provide specific cost estimations for EACH
item in the itinerary, including transportation, accommodation,
activities, meals, and shows.

At the end of the itinerary, please provide:
* **Total Estimated Cost:** $[total cost]
* **Remaining Budget:** $[remaining budget]
* **Budget Utilization:** [total cost]/[budget]
"""
```

**预算管理特点:**
- 详细成本估算
- 智能预算分配
- 实时预算监控

### 3. 多模态信息整合

系统整合了多种类型的信息：
- **景点信息**: 描述、地址、网站、提示
- **餐厅推荐**: 位置、菜系、价格范围
- **交通信息**: 航班、地铁、出租车
- **住宿选择**: 酒店、Airbnb、价格

## 📈 性能优化

### 1. 缓存机制

```python
# 嵌入向量缓存
self.embedding_cache = {}

# 检查缓存
if query in self.embedding_cache:
    query_embedding = self.embedding_cache[query]
else:
    query_embedding = get_embedding(query)
    self.embedding_cache[query] = query_embedding
```

**优化效果:**
- 减少重复的API调用
- 提高响应速度
- 降低API成本

### 2. 向量索引优化

```python
# 使用Faiss的L2索引
self.index = faiss.IndexFlatL2(embedding_dim)

# 批量添加向量
self.index.add(np.array(self.knowledge_embeddings))
```

**优化效果:**
- 高效的相似度搜索
- 支持大规模向量数据
- 内存使用优化

## 🔮 未来发展方向

### 1. 技术增强

- **多模态支持**: 整合图像、音频信息
- **实时数据**: 接入实时交通、天气数据
- **个性化学习**: 基于用户历史行为优化推荐

### 2. 功能扩展

- **多城市支持**: 扩展到全球主要城市
- **社交功能**: 用户评价和推荐
- **预订集成**: 直接预订机票、酒店

### 3. 架构优化

- **微服务架构**: 提高系统可扩展性
- **分布式部署**: 支持高并发访问
- **边缘计算**: 减少网络延迟

## 📚 参考文献

1. **Reimers, Nils, and Iryna Gurevych.** "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks." *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing* (2019): 3982–3992.

2. **Lewis, Mike et al.** "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." *Advances in Neural Information Processing Systems 33* (2020): 9459–9474.

3. **Johnson, Jeff et al.** "Billion-scale similarity search with GPUs." *IEEE Transactions on Big Data 7* (2021): 535–547.

4. **Shuster, Kurt, et al.** "Retrieval Augmentation Reduces Hallucination in Conversation." *arXiv preprint arXiv:2104.07567* (2021).

## 👨‍💻 作者信息

**Frank Morales Aguilera, BEng, MEng, SMIEEE**  
Boeing Associate Technical Fellow /Engineer /Scientist /Inventor /Cloud Solution Architect /Software Developer @ Boeing Global Services

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

---

**⭐ 如果这个项目对您有帮助，请给个Star支持！⭐** 