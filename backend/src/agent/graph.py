
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

    prompt = ChatPromptTemplate.from_messages([('system',"your are helpful assistant , summarize the content given anser in bulletp point , max 5 point "),("human","{context}")]).format_messages(context=context)
    summary = stream_model.invoke(prompt)
    return {"messages": [summary]}

# Setup the graph
builder = StateGraph(MessagesState)
builder.add_node("summarize", summarize_node)

builder.add_edge(START,"summarize")

graph  = builder.compile()



# input = """The majority of GNNs are Graph Convolutional Networks, and it is important to learn about them before jumping into a node classification tutorial.  

# The convolution in GCN is the same as a convolution in convolutional neural networks. It multiplies neurons with weights (filters) to learn from data features. 

# It acts as sliding windows on whole images to learn features from neighboring cells. The filter uses weight sharing to learn various facial features in image recognition systems - Towards Data Science. 

# Now transfer the same functionality to Graph Convolutional networks where a model learns the features from neighboring nodes. The major difference between GCN and CNN is that it is developed to work on non-euclidean data structures where the order of nodes and edges can vary. """

# res = graph.invoke({'messages':[HumanMessage(content=f"{input}")]})

# print(res['messages'][-1].content)




# from langgraph.checkpoint.memory import InMemorySaver
# from langgraph.graph import StateGraph, END,START ,MessagesState
# from langchain_core.messages import SystemMessage, HumanMessage,AIMessage,ToolMessage

# from langchain.prompts import ChatPromptTemplate

# from typing import TypedDict, List,Annotated
# from langchain_google_genai import ChatGoogleGenerativeAI

# # model = ChatGoogleGenerativeAI(model='gemini-2.0-flash',api_key="AIzaSyDK1CNcAh***********k2U51Rug",disable_streaming=True)
# stream_model = ChatGoogleGenerativeAI(model='gemini-1.5-flash',api_key="AIzaSy**************k2U51Rug")



# from langgraph.config import get_stream_writer

# import time

# def summarize_node(state:MessagesState):
#     writer =get_stream_writer()
#     message = state['messages'][-1].content
#     writer('starting summarazing topic.......')
#     # print(state['messages'][-1])
#     # summary  = f"""this is  summamry on given by llm on  topic}"""
#     context = state["messages"][-1].content
#     # print(context)

#     prompt = ChatPromptTemplate.from_messages([('system',"your are helpful assistant , summarize the content given by user  in ~50 word to ~100 word"),("human","{context}")]).format_messages(context=context)
#     summary = stream_model.invoke(prompt)
#     return {"messages": [summary]}

# # Setup the graph
# builder = StateGraph(MessagesState)
# builder.add_node("summarize", summarize_node)

# builder.add_edge(START,"summarize")

# graph  = builder.compile()

