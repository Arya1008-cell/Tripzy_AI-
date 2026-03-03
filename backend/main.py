from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_chain import generate_itinerary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelRequest(BaseModel):
    current_city: str
    destination_city: str
    days: int
    budget: str
    style: str

@app.post("/generate-itinerary")
async def create_itinerary(request: TravelRequest):
    # Using the data from the request to trigger the AI Agent
    result = generate_itinerary(request.dict())
    return {"itinerary": result}     