#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI旅行规划系统 - 使用示例
========================

本文件展示了如何配置和使用AI旅行规划系统的完整流程。
包含环境配置、系统初始化、参数设置和结果分析。

作者: Frank Morales Aguilera
"""

import os
import sys
import json
from datetime import datetime, timedelta

# 添加项目路径到系统路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入AI旅行规划系统
from TRAVEL_ASI_DEMO_GPT_中文注释版 import Agent, get_embedding, nyc_knowledge

class TravelPlannerDemo:
    """
    AI旅行规划系统演示类
    
    提供完整的使用示例，包括：
    1. 系统初始化
    2. 参数配置
    3. 旅行计划生成
    4. 结果分析
    """
    
    def __init__(self):
        """初始化演示环境"""
        self.agent = None
        self.setup_environment()
    
    def setup_environment(self):
        """
        设置运行环境
        
        检查必要的环境变量和依赖
        """
        print("🔧 正在设置运行环境...")
        
        # 检查OpenAI API密钥
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("❌ 错误: 未找到OPENAI_API_KEY环境变量")
            print("请设置您的OpenAI API密钥:")
            print("export OPENAI_API_KEY='your_api_key_here'")
            sys.exit(1)
        
        print("✅ OpenAI API密钥已配置")
        
        # 检查其他依赖
        try:
            import openai
            import faiss
            import numpy as np
            print("✅ 所有依赖包已安装")
        except ImportError as e:
            print(f"❌ 错误: 缺少依赖包 - {e}")
            print("请运行: pip install openai faiss-cpu numpy")
            sys.exit(1)
    
    def initialize_agent(self):
        """
        初始化AI旅行代理
        
        创建代理实例并加载知识库
        """
        print("\n🤖 正在初始化AI旅行代理...")
        
        # 创建代理实例
        self.agent = Agent(
            name="NYCAI",
            cache_size=1000,
            embedding_dim=1536
        )
        
        # 加载纽约旅行知识库
        print("📚 正在加载纽约旅行知识库...")
        self.agent.load_knowledge(nyc_knowledge)
        
        print("✅ AI旅行代理初始化完成")
    
    def get_user_preferences(self):
        """
        获取用户旅行偏好
        
        返回:
            dict: 包含用户偏好的字典
        """
        print("\n📝 请提供您的旅行偏好:")
        
        # 旅行日期
        start_date = input("出发日期 (YYYY-MM-DD): ") or "2024-04-10"
        end_date = input("返回日期 (YYYY-MM-DD): ") or "2024-04-15"
        
        # 预算
        budget = input("预算金额 (美元): ") or "10000"
        
        # 交通偏好
        transport_mode = input("交通方式 (airplane/train/bus/car): ") or "airplane"
        
        # 住宿偏好
        accommodation_type = input("住宿类型 (hotel/Airbnb): ") or "hotel"
        
        # 旅行偏好
        preferences = input("旅行偏好描述: ") or "I prefer cultural experiences and local food"
        
        # 兴趣列表
        interests_input = input("兴趣列表 (用逗号分隔): ") or "museums, Broadway shows, Central Park"
        interests = [interest.strip() for interest in interests_input.split(",")]
        
        return {
            "travel_dates": [start_date, end_date],
            "budget": f"${budget}",
            "transport_mode": transport_mode,
            "accommodation_type": accommodation_type,
            "preferences": preferences,
            "interests": interests
        }
    
    def generate_travel_plan(self, user_prefs):
        """
        生成个性化旅行计划
        
        参数:
            user_prefs (dict): 用户偏好字典
        """
        print("\n🚀 正在生成您的个性化旅行计划...")
        print("="*60)
        
        # 显示用户偏好
        print("📋 您的旅行偏好:")
        print(f"   📅 旅行日期: {user_prefs['travel_dates'][0]} 到 {user_prefs['travel_dates'][1]}")
        print(f"   💰 预算: {user_prefs['budget']}")
        print(f"   🚗 交通方式: {user_prefs['transport_mode']}")
        print(f"   🏨 住宿类型: {user_prefs['accommodation_type']}")
        print(f"   🎯 偏好: {user_prefs['preferences']}")
        print(f"   ❤️ 兴趣: {', '.join(user_prefs['interests'])}")
        print("="*60)
        
        # 生成旅行计划
        self.agent.plan_nyc_trip(
            travel_dates=user_prefs['travel_dates'],
            budget=user_prefs['budget'],
            preferences=user_prefs['preferences'],
            interests=user_prefs['interests']
        )
    
    def analyze_results(self, user_prefs):
        """
        分析生成的旅行计划
        
        参数:
            user_prefs (dict): 用户偏好字典
        """
        print("\n📊 旅行计划分析:")
        print("="*40)
        
        # 计算旅行天数
        start_date = datetime.strptime(user_prefs['travel_dates'][0], "%Y-%m-%d")
        end_date = datetime.strptime(user_prefs['travel_dates'][1], "%Y-%m-%d")
        num_days = (end_date - start_date).days
        
        print(f"📅 旅行天数: {num_days} 天")
        print(f"💰 预算: {user_prefs['budget']}")
        print(f"🎯 主要兴趣: {', '.join(user_prefs['interests'])}")
        
        # 分析兴趣分布
        print("\n🎨 兴趣分析:")
        for interest in user_prefs['interests']:
            print(f"   • {interest}")
        
        print("\n✅ 旅行计划生成完成！")
    
    def run_demo(self):
        """
        运行完整的演示流程
        """
        print("🎉 欢迎使用AI旅行规划系统！")
        print("="*60)
        
        try:
            # 1. 初始化代理
            self.initialize_agent()
            
            # 2. 获取用户偏好
            user_prefs = self.get_user_preferences()
            
            # 3. 生成旅行计划
            self.generate_travel_plan(user_prefs)
            
            # 4. 分析结果
            self.analyze_results(user_prefs)
            
        except KeyboardInterrupt:
            print("\n\n⏹️ 用户中断了程序")
        except Exception as e:
            print(f"\n❌ 发生错误: {e}")
            import traceback
            traceback.print_exc()

def run_quick_demo():
    """
    快速演示 - 使用预设参数
    """
    print("🚀 AI旅行规划系统 - 快速演示")
    print("="*50)
    
    # 预设参数
    demo_prefs = {
        "travel_dates": ["2024-04-10", "2024-04-15"],
        "budget": "$10000",
        "transport_mode": "airplane",
        "accommodation_type": "hotel",
        "preferences": "I prefer a mix of sightseeing, cultural experiences, and trying local food. I like to walk a lot but also want to use public transport.",
        "interests": ["museums", "Broadway shows", "Central Park"]
    }
    
    try:
        # 初始化系统
        demo = TravelPlannerDemo()
        demo.initialize_agent()
        
        # 生成旅行计划
        demo.generate_travel_plan(demo_prefs)
        
        # 分析结果
        demo.analyze_results(demo_prefs)
        
    except Exception as e:
        print(f"❌ 演示过程中发生错误: {e}")

def test_vector_search():
    """
    测试向量搜索功能
    """
    print("🔍 测试向量搜索功能")
    print("="*30)
    
    try:
        # 创建代理
        agent = Agent("TestAgent", cache_size=100)
        agent.load_knowledge(nyc_knowledge)
        
        # 测试查询
        test_queries = [
            "museums and art galleries",
            "fine dining restaurants",
            "outdoor activities",
            "cultural experiences"
        ]
        
        for query in test_queries:
            print(f"\n🔎 查询: {query}")
            results = agent.retrieve_knowledge(query)
            print(f"📋 找到 {len(results)} 个相关结果")
            
            for i, result in enumerate(results[:2], 1):  # 只显示前2个结果
                name = list(result.keys())[0]
                description = result.get('description', 'N/A')
                print(f"   {i}. {name}: {description[:100]}...")
    
    except Exception as e:
        print(f"❌ 测试失败: {e}")

def main():
    """
    主函数 - 提供多种运行模式
    """
    print("🎯 AI旅行规划系统 - 使用示例")
    print("="*50)
    print("请选择运行模式:")
    print("1. 完整演示 (交互式)")
    print("2. 快速演示 (预设参数)")
    print("3. 测试向量搜索")
    print("4. 退出")
    
    while True:
        choice = input("\n请输入选择 (1-4): ").strip()
        
        if choice == "1":
            demo = TravelPlannerDemo()
            demo.run_demo()
            break
        elif choice == "2":
            run_quick_demo()
            break
        elif choice == "3":
            test_vector_search()
            break
        elif choice == "4":
            print("👋 再见！")
            break
        else:
            print("❌ 无效选择，请重新输入")

if __name__ == "__main__":
    main() 