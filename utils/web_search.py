from duckduckgo_search import DDGS

def web_search(query, max_results=3):
    try:
        with DDGS() as ddgs:
            results = [r["body"] for r in ddgs.text(query, max_results=max_results)]
        return " ".join(results) if results else "No relevant information found."
    except Exception as e:
        return f"⚠️ Web search error: {e}"
