from langgraph.graph import StateGraph
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from utils import crawl_with_tavily
from typing import TypedDict, Optional

# 🧠 Local Embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 🗃️ Vector Store
vectorstore = Chroma(embedding_function=embedding, persist_directory="vector_db")

# 🧠 Local LLM via Ollama
llm = Ollama(model="llama3")

# ✅ Define the state schema
class AgentState(TypedDict):
    query: str
    documents_added: Optional[bool]
    final_answer: Optional[str]

def build_agent_graph(tavily_api_key: str):
    graph = StateGraph(AgentState)  

    def research_agent(state: AgentState) -> AgentState:
        query = state["query"]
        raw_text = crawl_with_tavily(query, tavily_api_key)
        vectorstore.add_texts([raw_text], metadatas=[{"source": "tavily"}])
        return {"query": query, "documents_added": True}

    def draft_answer_agent(state: AgentState) -> AgentState:
        query = state["query"]
        retriever = vectorstore.as_retriever()
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        answer = qa_chain.run(query)
        return {"query": query, "final_answer": answer}

    graph.add_node("Research", research_agent)
    graph.add_node("AnswerDraft", draft_answer_agent)
    graph.set_entry_point("Research")
    graph.add_edge("Research", "AnswerDraft")
    graph.set_finish_point("AnswerDraft")

    return graph.compile()
