import json
from langchain import hub
from langchain.agents import create_openai_tools_agent
from langchain_openai.chat_models import ChatOpenAI
from tools import *
from dotenv import load_dotenv

load_dotenv()

prompt = hub.pull("hwchase17/openai-functions-agent")

# Choose the LLM that will drive the agent
llm = ChatOpenAI(temperature = 0)

# Construct the OpenAI Functions agent
agent_runnable = create_openai_tools_agent(llm, tools, prompt)

def run_query_agent(state: list):
    print("> Run the Agent")
    agent_out = agent_runnable.invoke(state)
    return {"agent_out": agent_out}

def execute_search(state: list):
    print("> Execute Search")
    action = state["agent_out"]
    tool_calls = action[-1].message_log[-1].additional_kwargs["tool_calls"]
    print(tool_calls)
    out = ''
    for tool_call in tool_calls:
        # print(tool_call)
        if(tool_call['function']['name'] == 'flight-search'):
            out += str(flight_search.invoke(json.loads(tool_call["function"]["arguments"])))
            
        elif(tool_call['function']['name'] == 'hotel-search'):
            out += str(hotel_search.invoke(json.loads(tool_call["function"]["arguments"])))

    print(out)
    return {"intermediate_steps": [{"search": out}]}
    
def router(state: list):
    print("> router")
    # print(state["agent_out"])
    if isinstance(state["agent_out"], list):
        return 'search'
    else:
        return "error"

final_answer_llm = llm.bind_tools([final_answer], tool_choice="final_answer")
def rag_final_answer(state: list):
    print("> final_answer")
    query = state["input"]
    data = state["intermediate_steps"][-1]

    prompt = f"""Your task is to output affordable airline itenaries based on the departure and destination location. Also, provide 3 best properties where he can stay at the destination. 
    Give response in `answer`, written in some good format. Note : Prices are in INR

    DATA: {data}

    QUESTION: {query}
    """
    out = final_answer_llm.invoke(prompt)
    function_call = out.additional_kwargs["tool_calls"][-1]["function"]["arguments"]
    return {"agent_out": function_call}

def handle_error(state: list):
    print("> handle_error")
    query = state["input"]
    prompt = f"""You are a helpful assistant, answer the user's question.

    QUESTION: {query}
    """
    out = final_answer_llm.invoke(prompt)
    function_call = out.additional_kwargs["tool_calls"][-1]["function"]["arguments"]
    return {"agent_out": function_call}
