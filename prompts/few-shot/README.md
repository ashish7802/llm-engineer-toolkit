# Few-Shot Prompt Templates

---

## 🏷️ Text Classification

```python
prompt = """Classify the sentiment of each review as: positive, negative, or neutral.

Review: "This product is amazing, works perfectly!"
Sentiment: positive

Review: "It's okay, nothing special."
Sentiment: neutral

Review: "Terrible quality, broke after one day."
Sentiment: negative

Review: "{USER_REVIEW}"
Sentiment:"""
```

---

## 🔎 Entity Extraction

```python
prompt = """Extract entities (Person, Organization, Location) from the text.
Return as JSON.

Text: "Elon Musk founded SpaceX in Hawthorne, California."
Entities: {"Person": ["Elon Musk"], "Organization": ["SpaceX"], "Location": ["Hawthorne, California"]}

Text: "Sundar Pichai is the CEO of Google, headquartered in Mountain View."
Entities: {"Person": ["Sundar Pichai"], "Organization": ["Google"], "Location": ["Mountain View"]}

Text: "{USER_TEXT}"
Entities:"""
```

---

## 📝 Summarization

```python
prompt = """Summarize the following text in 2-3 sentences. Keep the key points.

Text: "Large language models (LLMs) are AI systems trained on massive text datasets..."
Summary: "LLMs are AI systems trained on large text corpora to understand and generate human language. They power applications like chatbots and code assistants."

Text: "{USER_TEXT}"
Summary:"""
```

---

## 🔄 Format Conversion

```python
prompt = """Convert the natural language description to a structured JSON object.

Input: "John is 28 years old and works as a software engineer at Google in San Francisco"
Output: {"name": "John", "age": 28, "job_title": "Software Engineer", "company": "Google", "city": "San Francisco"}

Input: "Sarah, 34, is a doctor at AIIMS Delhi"
Output: {"name": "Sarah", "age": 34, "job_title": "Doctor", "company": "AIIMS", "city": "Delhi"}

Input: "{USER_INPUT}"
Output:"""
```
