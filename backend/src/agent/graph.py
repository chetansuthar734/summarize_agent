
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, END,START ,MessagesState
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage,ToolMessage


from typing import TypedDict, List,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',api_key="AIzaSyDK1CNcAhSrM4qy3UVIXLu7J7Qk2U51Rug",disable_streaming=True)
stream_model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',api_key="AIzaSyDK1CNcAhSrM4qy3UVIXLu7J7Qk2U51Rug")



from langgraph.config import get_stream_writer

import time

def summarize_node(state:MessagesState):
    writer =get_stream_writer()
    topic = state['messages'][-1].content
    writer('starting summarazing topic.......')
    time.sleep(2)
    history = "\n".join(msg.content for msg in state["messages"])
    summary  = f"""this is  summamry on given by llm on  topic:{topic}"""
    # summary = stream_model.invoke([{"role": "system", "content": "Summarize the following conversation:"},
                        #   {"role": "assistant", "content": history}])
    return {"messages": [AIMessage(content=summary)]}

# Setup the graph
builder = StateGraph(MessagesState)
builder.add_node("summarize", summarize_node)

builder.add_edge(START,"summarize")

graph  = builder.compile()
