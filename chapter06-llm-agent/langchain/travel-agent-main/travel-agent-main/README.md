# LangGraph Travel Agent

This repository contains a basic implementation of a travel agent using LangGraph. The travel agent takes user queries, searches for flight and hotel details at the desired destination, and provides personalized recommendations.

## Getting Started

Follow these instructions to set up and run the travel agent on your local machine.

### Prerequisites

Ensure you have the following python version:

- Python 3.11+

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/2020uce0047/travel-agent.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd langgraph-travel-agent
    ```

3. **Create a `.env` file in the parent directory** and add your API keys:

    ```env
    OPENAI_API_KEY = your-openai-key
    SERP_API_KEY = your-serpapi-key
    ```

4. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Open a terminal in the parent directory**.
2. **Run the Streamlit application**:

    ```bash
    streamlit run main.py
    ```

The application should now be running on `http://localhost:8501`. Open this URL in your browser to interact with the travel agent.

## Contributing

Feel free to fork this repository and submit pull requests. Your contributions are welcome!
