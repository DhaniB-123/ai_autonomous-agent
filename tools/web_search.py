from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise RuntimeError("tavily api key not found in .env file")

def get_response(query : str):
    client = TavilyClient(api_key=api_key)
    response = client.search(query)
    result  = response["results"]
    return "\n\n".join([r["content"][:300] for r in result])



web_search_tool = {
    "type" : "function",
    "function" : {
        "name" : "web_search_tool",
        "description" : "search the web for the real time information",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "query" : {
                    "type" : "string",
                    "description" : "the search query",
                }
            },
            "required" : ["query"]
        }
    }
}
