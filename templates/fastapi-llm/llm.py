import os
from anthropic import AsyncAnthropic
from typing import AsyncIterator
import json

class LLMClient:
    def __init__(self):
        self.client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.model = "claude-3-5-sonnet-20241022"

    async def chat(
        self,
        messages: list[dict],
        system: str = "You are a helpful assistant.",
        max_tokens: int = 1024,
    ) -> str:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        )
        return response.content[0].text

    async def stream(
        self,
        messages: list[dict],
        system: str = "You are a helpful assistant.",
        max_tokens: int = 1024,
    ) -> AsyncIterator[str]:
        async with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
        ) as stream:
            async for text in stream.text_stream:
                yield json.dumps({"token": text})
