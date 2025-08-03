"""
AI旅行规划系统 - 基于RAG和CAG技术的智能旅行助手
==================================================

作者: Frank Morales Aguilera, BEng, MEng, SMIEEE
Boeing Associate Technical Fellow /Engineer /Scientist /Inventor /Cloud Solution Architect /Software Developer

技术架构:
- OpenAI Embedding Model (text-embedding-ada-002): 用于文本向量化
- GPT-4 Language Model: 用于生成个性化旅行计划
- Faiss向量数据库: 用于高效相似度搜索
- Cache-Augmented Generation (CAG): 缓存增强生成技术

核心创新:
1. 结合RAG和CAG技术，实现高效的知识检索和生成
2. 使用向量化技术进行个性化内容推荐
3. 智能预算管理和行程优化
4. 多模态信息整合（景点、餐厅、交通等）

系统优势:
- 高度个性化: 基于用户偏好和历史行为
- 实时响应: 缓存机制减少延迟
- 成本可控: 智能预算分配
- 信息丰富: 整合多源数据
"""

# ==================== 环境依赖安装 ====================
"""
安装必要的Python包:
- openai: OpenAI API客户端
- faiss-cpu: Facebook AI Similarity Search (CPU版本)
- tiktoken: OpenAI的tokenizer
- numpy: 数值计算
- json: JSON数据处理
- re: 正则表达式
- datetime: 日期时间处理
"""

# ==================== 导入必要的库 ====================
from IPython import get_ipython
from IPython.display import display
import openai
import faiss
import numpy as np
import tiktoken
import os
import json
import re
import datetime
import colab_env  # Google Colab环境支持

from openai import OpenAI

# ==================== OpenAI客户端初始化 ====================
"""
初始化OpenAI客户端，用于调用GPT-4和Embedding模型
API密钥从环境变量中获取，确保安全性
"""
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ==================== 文本向量化函数 ====================
def get_embedding(text, model="text-embedding-ada-002"):
    """
    获取文本的向量表示（嵌入向量）
    
    参数:
        text (str): 需要向量化的文本
        model (str): 使用的嵌入模型，默认使用OpenAI的text-embedding-ada-002
    
    返回:
        list: 文本的向量表示（1536维向量）
    
    技术原理:
        - 将文本转换为数值向量，捕捉语义信息
        - 相似含义的文本会产生相似的向量
        - 支持后续的相似度搜索和内容推荐
    """
    # 清理文本，移除换行符
    text = text.replace("\n", " ")
    
    # 调用OpenAI API获取嵌入向量
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# ==================== AI旅行代理类 ====================
class Agent:
    """
    AI旅行代理类 - 核心智能体
    
    功能:
    1. 知识库管理: 加载和管理旅行相关信息
    2. 智能检索: 基于用户偏好检索相关内容
    3. 行程规划: 生成个性化旅行计划
    4. 结果展示: 格式化输出旅行建议
    
    技术特点:
    - 使用Faiss进行高效的向量相似度搜索
    - 实现缓存机制提高响应速度
    - 支持多维度信息整合
    """

    def __init__(self, name, cache_size, embedding_dim=1536):
        """
        初始化AI代理
        
        参数:
            name (str): 代理名称
            cache_size (int): 缓存大小
            embedding_dim (int): 向量维度，默认1536（OpenAI ada-002模型）
        """
        self.name = name
        self.cache_size = cache_size
        self.embedding_dim = embedding_dim
        
        # 初始化Faiss索引 - 用于向量相似度搜索
        # IndexFlatL2: 使用L2距离进行相似度计算
        self.index = faiss.IndexFlatL2(embedding_dim)
        
        # 存储知识库的向量和原始数据
        self.knowledge_embeddings = []  # 向量数据
        self.knowledge_data = []        # 原始文本数据
        
        # 嵌入向量缓存 - 避免重复计算
        self.embedding_cache = {}

    def load_knowledge(self, knowledge_data):
        """
        加载旅行知识库到Faiss索引
        
        参数:
            knowledge_data (dict): 包含旅行信息的JSON对象
        
        技术流程:
        1. 遍历知识库中的每个景点/信息
        2. 将文本转换为向量表示
        3. 存储向量和原始数据
        4. 构建Faiss索引用于快速检索
        
        知识库结构示例:
        {
            "attractions": {
                "景点名称": {
                    "description": "景点描述",
                    "address": "地址",
                    "website": "网站",
                    "tips": ["提示1", "提示2"]
                }
            }
        }
        """
        # 遍历知识库的每个类别和子类别
        for category, subcategories in knowledge_data.items():
            for key, value in subcategories.items():
                # 检查缓存中是否已有该文本的向量
                if key in self.embedding_cache:
                    embedding = self.embedding_cache[key]
                else:
                    # 获取文本的向量表示
                    embedding = get_embedding(key, model='text-embedding-ada-002')
                    # 缓存向量结果
                    self.embedding_cache[key] = embedding
                
                # 存储向量和原始数据
                self.knowledge_embeddings.append(embedding)
                self.knowledge_data.append(value)

        # 将所有向量添加到Faiss索引中
        self.index.add(np.array(self.knowledge_embeddings))

    def retrieve_knowledge(self, query):
        """
        基于查询检索相关知识
        
        参数:
            query (str): 用户查询文本
        
        返回:
            list: 相关的知识条目列表
        
        技术原理:
        1. 将查询文本转换为向量
        2. 使用Faiss进行相似度搜索
        3. 返回最相关的5个结果
        4. 利用缓存机制提高效率
        """
        # 检查查询是否已缓存
        if query in self.embedding_cache:
            query_embedding = self.embedding_cache[query]
        else:
            # 获取查询的向量表示
            query_embedding = get_embedding(query, model='text-embedding-ada-002')
            self.embedding_cache[query] = query_embedding

        # 使用Faiss进行相似度搜索，返回最相关的5个结果
        # D: 距离矩阵，I: 索引矩阵
        D, I = self.index.search(np.array([query_embedding]), k=5)

        # 根据索引获取相关的知识条目
        relevant_info = []
        for i in I[0]:
            relevant_info.append(self.knowledge_data[i])
        return relevant_info

    def plan_nyc_trip(self, travel_dates, budget, preferences, interests):
        """
        生成个性化的纽约旅行计划
        
        参数:
            travel_dates (list): 旅行日期 [开始日期, 结束日期]
            budget (str): 预算金额
            preferences (str): 用户偏好描述
            interests (list): 用户兴趣列表
        
        核心功能:
        1. 收集用户偏好（交通方式、住宿类型）
        2. 检索相关知识
        3. 生成详细的旅行计划
        4. 包含成本估算和实用建议
        
        技术亮点:
        - 使用CAG技术将相关知识直接嵌入到GPT-4的上下文中
        - 结构化的提示词设计确保输出格式一致
        - 智能预算分配和成本控制
        """
        # 收集用户的交通和住宿偏好
        print("正在收集您的旅行偏好...")
        transport_mode = input("Preferred mode of transport (airplane, train, bus, car): ")
        accommodation_type = input("Preferred accommodation type (hotel, Airbnb): ")

        # 检索与用户偏好相关的知识
        relevant_knowledge = self.retrieve_knowledge(preferences)
        for interest in interests:
            relevant_knowledge += self.retrieve_knowledge(interest)

        # 构建详细的系统提示词
        system_prompt = f"""You are an expert travel agent specializing in NYC.
                Create a detailed itinerary that includes transportation
                from Montreal to NYC and accommodation in NYC.
                The preferred mode of transport is {transport_mode} and
                the preferred accommodation type is {accommodation_type}.

                The user wants to visit Yankee Stadium and prefers upscale
                hotels and dining experiences.

                For the Yankee Stadium visit, suggest one of the following
                premium seating options: the Legends Suite Club, the Ford Field
                MVP Club, or the Champion Suite. Do NOT suggest just a basic tour.

                On the day of the Yankee Stadium visit, the dinner will be
                INSIDE the stadium, either at the Legends Suite Club,
                the Ford Field MVP Club, or the Champion Suite.

                The Yankee Stadium visit should be scheduled in the AFTERNOON
                or EVENING, as baseball games are not typically played in
                the morning.

                Use the following format:

                **Transportation:**
                * [Flight/Train details] ([Estimated Cost: $xxx])

                **Accommodation:**
                * [Hotel details] ([Estimated Cost per night: $xxx])

                **Day 1:**
                * **Morning:** [Activity 1] ([Estimated Cost: $xx]) - [Brief Description]
                * **Afternoon:** [Activity 2] ([Estimated Cost: $xx]) - [Brief Description]
                * **Evening:** [Activity 3] ([Estimated Cost: $xx]) - [Brief Description]
                * **Dinner:** [Restaurant Suggestion] ([Estimated Cost per person: $xx])

                **Day 2:**
                * ... and so on ...

                Include transportation suggestions, estimated costs, and practical tips.
                Consider the user's budget: $10000

                It's crucial that you provide specific cost estimations for EACH
                item in the itinerary, including transportation, accommodation,
                activities, meals, and shows.  Do NOT use general price ranges
                like "expensive" or "$$$" as these are not helpful for budget
                planning.  Instead, provide numerical estimates like "$25", "$150",
                or "$40-$60".

                At the end of the itinerary, please provide the following:
                * **Total Estimated Cost:** $[total cost]
                * **Remaining Budget:** $[remaining budget]
                * **Budget Utilization:** [total cost]/[budget]
                """

        # 构建用户查询
        user_query = f"""Plan a NYC trip from {travel_dates[0]} to {travel_dates[1]}.
                The traveler's preferences are: {preferences} and their interests include: {', '.join(interests)}.

                Here's some relevant information about NYC: {self.summarize_knowledge(relevant_knowledge)}
                """

        # 调用GPT-4生成旅行计划
        print("🤖 AI正在为您生成个性化旅行计划...")
        response = client.chat.completions.create(
            model="gpt-4",  # 使用GPT-4模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            max_tokens=4096  # 最大输出token数
        )

        # 输出AI生成的旅行计划
        print('\n')
        print(f"🎉 您的个性化旅行计划已生成:")
        print(f"{response.choices[0].message.content}")

        # 处理和展示旅行计划
        self.present_itinerary(response.choices[0].message.content, budget, travel_dates)

    def present_itinerary(self, itinerary_text, budget, travel_dates):
        """
        处理和展示旅行计划
        
        参数:
            itinerary_text (str): GPT-4生成的旅行计划文本
            budget (str): 预算金额
            travel_dates (list): 旅行日期
        
        功能:
        1. 解析旅行计划文本
        2. 计算旅行天数
        3. 格式化输出
        4. 预算分析和建议
        """
        # 使用正则表达式分割旅行计划的不同部分
        # 匹配: Transportation:, Accommodation:, Day X:
        sections = re.split(r"(Transportation:|Accommodation:|Day\s+\d+:)", itinerary_text)
        
        # 解析各个部分
        itinerary = {}
        current_section = None
        
        for section in sections:
            section = section.strip()
            if not section:
                continue
            if section in ("Transportation:", "Accommodation:"):
                current_section = section
                itinerary[current_section] = []
            elif re.match(r"Day\s+\d+:", section):
                current_section = section
                itinerary[current_section] = []
            elif current_section:
                itinerary[current_section].append(section)

        # 计算旅行天数
        start_date = datetime.datetime.strptime(travel_dates[0], "%Y-%m-%d")
        end_date = datetime.datetime.strptime(travel_dates[1], "%Y-%m-%d")
        num_days = (end_date - start_date).days

        # 格式化输出旅行计划
        print("\n" + "="*50)
        print("📋 您的详细旅行计划")
        print("="*50)
        
        for section, items in itinerary.items():
            print(f"\n{section}")
            print("-" * 30)
            for item in items:
                print(item)
            print("-" * 20)

    def summarize_knowledge(self, knowledge_list):
        """
        总结相关知识用于GPT-4提示词
        
        参数:
            knowledge_list (list): 知识条目列表
        
        返回:
            str: 格式化的知识摘要
        
        功能:
        将检索到的知识转换为适合GPT-4理解的格式
        """
        if not knowledge_list:
            return ""
        
        summary = ""
        for item in knowledge_list:
            # 获取知识条目的名称
            name = list(item.keys())[0]
            summary += f"**{name}**\n"
            summary += f"Description: {item.get('description', 'N/A')}\n"
            
            # 添加地址信息（如果有）
            if "address" in item:
                summary += f"Address: {item['address']}\n"
            
            # 添加网站信息（如果有）
            if "website" in item:
                summary += f"Website: {item['website']}\n"
            
            # 添加提示信息（如果有）
            if "tips" in item:
                summary += "Tips:\n" + "\n".join(item['tips']) + "\n"
            
            summary += "\n"
        return summary

# ==================== 纽约旅行知识库 ====================
"""
纽约旅行知识库 - 包含景点、餐厅、交通等信息
使用JSON格式存储，便于扩展和维护

知识库特点:
1. 结构化存储: 按类别组织信息
2. 详细信息: 包含描述、地址、网站、提示等
3. 可扩展性: 易于添加新的景点和信息
4. 多维度信息: 涵盖景点、餐厅、交通等多个方面
"""
nyc_knowledge = {
    "attractions": {
        "Empire State Building": {
            "description": "Iconic skyscraper with observation decks offering stunning views of the city.",
            "address": "350 Fifth Avenue, Manhattan",
            "website": "www.esbnyc.com",
            "tips": [
                "Purchase tickets online in advance to avoid long lines.",
                "Visit during the day and at night for different perspectives."
            ]
        },
        "Central Park": {
            "description": "A vast green oasis in the heart of Manhattan, perfect for picnics, walks, bike rides, and boating.",
            "activities": [
                "visit the Central Park Zoo",
                "rent a rowboat on The Lake",
                "see a performance at the Delacorte Theater",
                "have a picnic on the Great Lawn"
            ],
            "tips": [
                "Download a map of the park to navigate its many paths and attractions."
            ]
        },
        "The Metropolitan Museum of Art": {
            "description": "One of the world's largest and finest art museums.",
            "address": "1000 Fifth Avenue, Manhattan",
            "website": "www.metmuseum.org",
            "tips": [
                "Allow ample time to explore the vast collection.",
                "Consider purchasing a guided tour for a more in-depth experience."
            ]
        }
        # 可以继续添加更多景点信息...
    }
}

# ==================== 主程序执行 ====================
def main():
    """
    主程序入口 - 演示AI旅行规划系统的完整功能
    """
    print("🚀 AI旅行规划系统启动")
    print("="*50)
    
    # 创建AI代理实例
    print("🤖 初始化AI旅行代理...")
    agent = Agent("NYCAI", cache_size=1000)
    
    # 加载旅行知识库
    print("📚 加载纽约旅行知识库...")
    agent.load_knowledge(nyc_knowledge)
    
    # 设置旅行参数
    travel_dates = ["2024-04-10", "2024-04-15"]  # 5天旅行
    budget = "$10000"  # 预算1万美元
    preferences = "I prefer a mix of sightseeing, cultural experiences, and trying local food. I like to walk a lot but also want to use public transport."
    interests = ["museums", "Broadway shows", "Central Park"]
    
    print(f"📅 旅行日期: {travel_dates[0]} 到 {travel_dates[1]}")
    print(f"💰 预算: {budget}")
    print(f"🎯 偏好: {preferences}")
    print(f"❤️ 兴趣: {', '.join(interests)}")
    print("="*50)
    
    # 生成个性化旅行计划
    agent.plan_nyc_trip(travel_dates, budget, preferences, interests)

# ==================== 技术原理解释 ====================
"""
系统技术架构详解:

1. 向量化技术 (Embedding):
   - 使用OpenAI的text-embedding-ada-002模型
   - 将文本转换为1536维向量
   - 捕捉语义相似性，支持智能检索

2. 向量数据库 (Faiss):
   - Facebook开发的相似度搜索库
   - 支持高维向量的快速检索
   - 使用L2距离计算相似度

3. 缓存增强生成 (CAG):
   - 将相关知识直接嵌入到LLM上下文中
   - 避免实时检索，提高响应速度
   - 简化系统架构

4. 大语言模型 (GPT-4):
   - 生成自然语言的旅行计划
   - 理解用户偏好和约束
   - 提供结构化的输出

5. 智能代理架构:
   - 协调各个组件的工作
   - 管理用户交互
   - 处理数据流和结果展示

系统优势:
- 高度个性化: 基于用户偏好的智能推荐
- 实时响应: 缓存机制减少延迟
- 信息丰富: 整合多源旅行数据
- 成本可控: 智能预算分配
- 易于扩展: 模块化设计
"""

if __name__ == "__main__":
    main() 