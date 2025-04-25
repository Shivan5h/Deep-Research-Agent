
# 🧠 Deep Research Agent

An advanced LangGraph-based Research Agent powered by LangChain and Ollama's LLaMA3, capable of understanding, retrieving, and answering complex research queries using vector search, document retrieval, and prompt engineering.

---

## 📦 Features

- 🌐 Internet-level Research from local documents and APIs  
- 🧠 LLaMA 3 Integration via Ollama for powerful LLM reasoning  
- 🧩 LangGraph for composable agent workflows  
- 🔍 Document-based Retrieval with context-based answers  
- 💡 Real-time Question Answering

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/deep-research-agent.git
cd deep-research-agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Install Ollama & Pull LLaMA 3 Model

Make sure [Ollama](https://ollama.com) is installed and running.

```bash
# Start Ollama server
ollama serve

# Pull the LLaMA3 model (if not already done)
ollama pull llama3
```

> ⚠️ If you see an error like `OllamaEndpointNotFoundError`, it means the model is missing or Ollama isn't running. Use the command above to fix it.

---

## 🚀 Running the Project

```bash
python app.py
```

You'll be prompted to enter a query, and the agent will use LangGraph's workflow to fetch the result.

---

## 📁 Project Structure

```
deep-research-agent/
├── app.py                 # Main application
├── agents.py              # LangGraph agents
├── tools/                 # Retrieval tools, vector store setup
├── data/                  # Sample documents or datasets
├── requirements.txt
└── README.md
```

---

## 🔍 Example Query

```txt
"Explain the impact of generative AI on stock market prediction models."
```

---

## 💡 Troubleshooting

- **Error**: `OllamaEndpointNotFoundError`
  - ✅ **Fix**: Run `ollama serve` and make sure you’ve pulled `llama3` with `ollama pull llama3`.
- Ensure Ollama is running on `localhost:11434`
- Make sure you’re not using an outdated version of LangChain. Use:
  ```bash
  pip install --upgrade langchain langchain-community langgraph
  ```

---

## 🧠 Credits

Built using:
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [Ollama](https://ollama.com/)
- LLaMA3 Model

---

## 📃 License

MIT License
