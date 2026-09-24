from fastapi import FastAPI
from agent.runner import get_responses
from schemas import UserQuery


app = FastAPI(title="Autonomous-research-agent")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/research")
def research(request : UserQuery):
    result = get_responses(request.query)
    return result 

