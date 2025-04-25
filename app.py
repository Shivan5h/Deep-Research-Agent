import streamlit as st
from agents import build_agent_graph

st.set_page_config(page_title="Deep Research AI (Ollama)", layout="wide")
st.title("🧠 Deep Research AI with Local LLM (Ollama)")

with st.sidebar:
    st.header("🔐 API Key")
    tavily_key = st.text_input("Tavily API Key", type="password")
    st.markdown("---")
    query = st.text_area("📝 Enter your research query:")
    run_button = st.button("🚀 Run Research")

if run_button:
    if not tavily_key or not query:
        st.warning("Please provide both a Tavily API Key and a research query.")
    else:
        with st.spinner("Running research agents..."):
            graph = build_agent_graph(tavily_key)
            result = graph.invoke({"query": query})
        st.success("✅ Research Complete")
        st.subheader("📄 Final Answer")
        st.write(result["final_answer"])
