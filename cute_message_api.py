from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing (change in production)
    allow_credentials=True,
    allow_methods=["*"]
)

# Cute messages database
messages = {
    1: "You are important and loved! 💖",
    2: "You make the world a brighter place! ☀️",
    3: "Keep smiling, your happiness is contagious! 😊",
    4: "You are stronger than you think! 💪",
    5: "Your kindness makes a difference! 🌸"
}

@app.get("/")
def greet():
    return {"message": "Hey Nuzhath! Welcome to your special messages! 💕"}

@app.get("/messages")
def get_messages():
    return {"messages": list(messages.keys())}

@app.get("/messages/{msg_id}")
def get_message(msg_id: int):
    return {"message": messages.get(msg_id, "Message not found 😢")}

# Run using: uvicorn cute_message_api:app --reload
