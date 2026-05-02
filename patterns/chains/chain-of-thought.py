"""
Chain-of-Thought (CoT) Prompting Pattern
-----------------------------------------
Force the model to reason step-by-step before answering.
Dramatically improves accuracy on complex reasoning tasks.
"""

from anthropic import Anthropic

client = Anthropic()


def cot_query(question: str, show_thinking: bool = True) -> dict:
    """
    Ask a question using Chain-of-Thought prompting.
    Returns both the reasoning and the final answer.
    """
    system = """You are a careful, logical thinker.
    
For every question:
1. Break it down into steps
2. Think through each step explicitly  
3. Then give your final answer

Format your response as:
<thinking>
[Your step-by-step reasoning here]
</thinking>
<answer>
[Your concise final answer here]
</answer>"""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        system=system,
        messages=[{"role": "user", "content": question}],
    )

    raw = response.content[0].text

    # Parse thinking and answer
    thinking = ""
    answer = ""

    if "<thinking>" in raw and "</thinking>" in raw:
        thinking = raw.split("<thinking>")[1].split("</thinking>")[0].strip()
    if "<answer>" in raw and "</answer>" in raw:
        answer = raw.split("<answer>")[1].split("</answer>")[0].strip()

    if show_thinking:
        print("🧠 Thinking:")
        print(thinking)
        print("\n✅ Answer:")
        print(answer)

    return {"thinking": thinking, "answer": answer}


# --- Zero-shot CoT (just add "Let's think step by step") ---
def zero_shot_cot(question: str) -> str:
    """Simplest CoT — just append the magic phrase."""
    prompt = f"{question}\n\nLet's think step by step."

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


# --- Example ---
if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Math problem with CoT")
    print("=" * 50)
    cot_query(
        "If a train travels 120km in 90 minutes, and then 80km in 40 minutes, "
        "what is its average speed for the whole journey?"
    )

    print("\n" + "=" * 50)
    print("Example 2: Logic puzzle with Zero-shot CoT")
    print("=" * 50)
    answer = zero_shot_cot(
        "There are 3 boxes. One has apples, one has oranges, one has both. "
        "All labels are wrong. You can pick one fruit from one box. "
        "How do you correctly label all boxes?"
    )
    print(answer)
