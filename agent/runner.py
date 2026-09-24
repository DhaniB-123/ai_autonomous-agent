from groq import Groq
from dotenv import load_dotenv
from tools.web_search import web_search_tool,get_response
import os
import json

SYSTEM_PROMPT = """your are a professional researcher,you have given a tool called web_search_tool you have to multiple research atleast do 3 to 5 searches,stop until and unless you have enough data based on the user query and after researching you have to response in this format:

# [Research Topic]

## Key Findings
## Analysis
## Sources"""


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("groq_api_key not found")

client = Groq(api_key=api_key)


def get_responses(message : str):
    Message = [{"role" : "system","content" : SYSTEM_PROMPT},
               {"role" : "user","content" : message}]

    tool_Call = True 

    while tool_Call:
    
        response = client.chat.completions.create(
            messages=Message,
            model="openai/gpt-oss-120b",
            tools=[web_search_tool]
        )
        tool_Call = response.choices[0].message.tool_calls
        Message.append(response.choices[0].message)
        
        if not tool_Call:
            return response.choices[0].message.content
            
        
        tool_name = tool_Call[0].function.name
        arguments = json.loads(tool_Call[0].function.arguments)
        result = get_response(arguments["query"])
        Message.append({"role" : "tool","tool_call_id" : tool_Call[0].id,"content" : str(result)})