## 集成 Google Drive 的 AI 驱动 RAG 聊天机器人

这个强大的工作流程创建了一个 AI 驱动的 RAG（检索增强生成）聊天机器人，它能够利用 Qdrant 矢量存储和 Google 的 Gemini AI 处理、存储并与 Google Drive 中的文档进行交互。

------

## 核心功能

### 📚 **文件处理与存储**

- **文档检索：** 从指定的 Google Drive 文件夹中自动检索文档。
- **文档分块：** 将检索到的文档处理并分割成易于管理的小块。
- **AI 元数据提取：** 利用人工智能提取文档元数据，以增强搜索和检索能力。
- **高效向量存储：** 将文档向量存储在 Qdrant 中，以便进行高效的检索。

### 💬 **智能聊天界面**

- **Google Gemini 支持：** 提供由 Google Gemini AI 提供支持的对话式聊天界面。
- **RAG 上下文检索：** 利用 RAG 技术从已存储的文档中检索相关的上下文信息。
- **聊天历史记录：** 将聊天历史记录保留在 Google Docs 中，以便于参考。
- **准确响应：** 提供准确、具有上下文感知能力的响应。

### 🗄️ **向量存储管理**

- **安全删除操作：** 具备通过人工验证的安全删除操作功能。
- **Telegram 通知：** 为重要操作（如删除）提供 Telegram 通知。
- **数据完整性：** 通过适当的版本控制维护数据完整性。
- **批量处理：** 支持文档的批量处理。

------

## 设置步骤

### **1. 配置 API 凭证**

- **Google Drive & Docs 访问：**
  - 设置对 Google Drive 和 Google Docs 的访问权限。
- **Gemini AI API：**
  - 配置 Google Gemini AI 的 API。
- **Qdrant 矢量存储连接：**
  - 设置与 Qdrant 矢量存储的连接。
- **Telegram Bot：**
  - 添加 Telegram 机器人以接收通知。
- **OpenAI API Key：**
  - 将 OpenAI API Key 添加到名为“**按文件 ID 删除 Qdrant 点**”的节点中（尽管主要使用 Gemini，但此节点可能需要 OpenAI API）。

### **2. 配置文档来源**

- **Google Drive 文件夹 ID：**
  - 设置您希望机器人检索文档的 Google Drive 文件夹 ID。
- **Qdrant 集合名称：**
  - 定义用于存储文档向量的 Qdrant 集合名称。
- **文档处理参数：**
  - 设置文档处理的相关参数（例如，分块大小、重叠等）。

### **3. 测试和部署**

- **验证文档处理：**
  - 确认文档能够被正确地检索、分块和处理。
- **测试聊天功能：**
  - 测试聊天机器人是否能正常工作，并提供准确的响应。
- **确认向量存储操作：**
  - 验证向量的存储、检索和删除操作是否正常。
- **检查通知系统：**
  - 确认 Telegram 通知系统是否按预期工作。

------

这个工作流程非常适合那些需要创建能够访问和理解大型文档存储库的智能聊天机器人的组织，通过 RAG 技术，该机器人可以保持上下文并提供准确的响应。

Pre requisite:
1. Vetrorize Tours and Activities information in Pinecone Vector Database 
(https://n8n.io/workflows/5085-convert-tour-pdfs-to-vector-database-using-google-drive-langchain-and-openai/)


## UI-Based Query with webhook connecting to Lovable
This flow uses a web UI built using Lovable to query contracts directly from a form interface.

### Webhook Setup for Lovable
Webhook Node
Method: POST
URL: your webhook url
Response: Using 'Respond to Webhook' Node

### Structured Output Parser
Sample structure:
  "itinerary": [
    {
      "dayNumber": 1,
      "date": "2024-07-15",
      "activities": [
        {
          "id": "1",
          "title": "Kuala Lumpur International Airport",
          "description": "Arrival at KLIA",
          "duration": "1 hour",
          "location": "KLIA",
          "type": "transport"
        },



### Lovable UI
User shall submit Destination or Activity Search
Receive response back via the response webhook in a JSON format. 

Data is sent via webhook to n8n and responded with the Package options


⚙️ Tools & Tech Stack
Component	            Tool Used
AI Embedding	            OpenAI text-embedding-3-small
Vector DB	            Pinecone
Chunking	            Recursive Text Splitter
AI Agent	            OpenAI GPT Chat
Structure Output Parser	    Parse Response data in structured JSON format
Automation	            n8n
UI Integration	Lovable (form-based)