from tavily import TavilyClient

def crawl_with_tavily(query: str, api_key: str) -> str:
    tavily_client = TavilyClient(api_key=api_key)
    response = tavily_client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        include_answer=True,
        include_raw_content=True
    )
    documents = [r.get("content", "").strip() for r in response.get("results", []) if r.get("content")]
    return "\n\n---\n\n".join(documents) if documents else "No relevant data found."
