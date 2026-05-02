from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]
    system_prompt: str = "You are a helpful assistant."
    max_tokens: int = 1024

class ChatResponse(BaseModel):
    content: str
    model: str
