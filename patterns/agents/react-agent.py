"""
ReAct Agent Pattern (Reason + Act)
------------------------------------
The agent thinks step-by-step, calls tools, 
observes results, and repeats until done.

Loop: Thought → Action → Observation → Thought → ...
"""

import json
import os
from anthropic import Anthropic

client = Anthropic()

# --- Define Tools ---
tools = [
    {
        "name": "calculator",
        "description": "Perform arithmetic calculations",
        "input_schema": {
            "type": "object",
            "properties": {
                "expression": {"type": "string", "description": "Math expression, e.g. '2 + 2 * 10'"}
            },
            "required": ["expression"],
        },
    },
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"],
        },
    },
]

# --- Tool Executor ---
def execute_tool(name: str, inputs: dict) -> str:
    if name == "calculator":
        try:
            result = eval(inputs["expression"])  # Use safer eval in production
            return str(result)
        except Exception as e:
            return f"Error: {e}"

    elif name == "get_weather":
        # Mock — replace with real API
        return f"Weather in {inputs['city']}: 28°C, Sunny ☀️"

    return "Tool not found"


# --- ReAct Loop ---
def run_agent(user_query: str, max_iterations: int = 5) -> str:
    messages = [{"role": "user", "content": user_query}]

    for i in range(max_iterations):
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            tools=tools,
            messages=messages,
        )

        # If done, return final answer
        if response.stop_reason == "end_turn":
            for block in response.content:
                if hasattr(block, "text"):
                    return block.text

        # If tool call needed
        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"🔧 Calling tool: {block.name}({block.input})")
                    result = execute_tool(block.name, block.input)
                    print(f"📊 Result: {result}")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result,
                    })

            messages.append({"role": "user", "content": tool_results})

    return "Max iterations reached."


# --- Example ---
if __name__ == "__main__":
    answer = run_agent("What is 25 * 4 + 100? Also what's the weather in Lucknow?")
    print(f"\n✅ Final Answer: {answer}")
