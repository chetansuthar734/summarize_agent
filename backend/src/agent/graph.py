
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, END,START ,MessagesState
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage,ToolMessage

from langchain.prompts import ChatPromptTemplate

from typing import TypedDict, List,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',api_key="AIzaSyDK1CNcAh***********k2U51Rug",disable_streaming=True)
stream_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key="AIzaSyDK1CNcAhSrM4qy3UVIXLu7J7Qk2U51Rug")



from langgraph.config import get_stream_writer

import time

def summarize_node(state:MessagesState):
    writer =get_stream_writer()
    message = state['messages'][-1].content
    writer('starting summarazing topic.......')
    # print(state['messages'][-1])
    # summary  = f"""this is  summamry on given by llm on  topic}"""
    context = state["messages"][-1].content
    # print(context)

    prompt = ChatPromptTemplate.from_messages([('system',"your are helpful assistant , summarize the content given by user  in ~50 word to ~100 word"),("human","{context}")]).format_messages(context=context)
    summary = stream_model.invoke(prompt)
    return {"messages": [summary]}

# Setup the graph
builder = StateGraph(MessagesState)
builder.add_node("summarize", summarize_node)

builder.add_edge(START,"summarize")

graph  = builder.compile()

