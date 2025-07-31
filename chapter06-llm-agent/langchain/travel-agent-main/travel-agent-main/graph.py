import operator
from typing import Annotated, TypedDict, Union
from langgraph.graph import StateGraph, END
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import BaseMessage
from agent import *

class AgentState(TypedDict):
    input: str
    chat_history: list[BaseMessage]
    agent_out: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]

def Graph():
    graph = StateGraph(AgentState)

    graph.add_node("query_agent", run_query_agent)
    graph.add_node("search", execute_search)
    graph.add_node("error", handle_error)
    graph.add_node("rag_final_answer", rag_final_answer)

    graph.set_entry_point("query_agent")

    # conditional edges are controlled by our router
    graph.add_conditional_edges(
        source = "query_agent",  # where in graph to start
        path = router,  # function to determine which node is called
        path_map ={
            "search": "search",
            "error": "error",
            "final_answer": END
        }
    )
    graph.add_edge("search", "rag_final_answer")
    graph.add_edge("error", END)
    graph.add_edge("rag_final_answer", END)

    runnable = graph.compile()
    return runnable