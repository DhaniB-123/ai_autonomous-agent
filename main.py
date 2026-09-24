from fastapi import FastAPI
from agent.runner import get_responses
from schemas import UserQuery


app = FastAPI(title="Autonomous-research-agent")


@app.post("/research")
def research(request : UserQuery):
    result = get_responses(request.query)
    return result 

