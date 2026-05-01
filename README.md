# 🧠 LLM Engineer Toolkit

> A practical, production-ready collection of prompts, patterns, templates, and resources for engineers building with Large Language Models.

[![GitHub stars](https://img.shields.io/github/stars/ashish7802/llm-engineer-toolkit?style=flat-square)](https://github.com/ashish7802/llm-engineer-toolkit/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

**Stop googling the same LLM patterns every project.** This toolkit gives you everything you need — from battle-tested prompt templates to production FastAPI boilerplates — in one place.

---

## 📦 What's Inside

| Folder | What you get |
|--------|-------------|
| [`/prompts`](./prompts) | System prompts, few-shot templates, CoT patterns |
| [`/patterns`](./patterns) | RAG, Agents, Chains — with working Python code |
| [`/templates`](./templates) | FastAPI + LangChain starter boilerplates |
| [`/resources`](./resources) | Curated papers, tools, courses |
| [`/examples`](./examples) | End-to-end real-world mini projects |

---

## 🚀 Quick Start

```bash
git clone https://github.com/ashish7802/llm-engineer-toolkit
cd llm-engineer-toolkit
pip install -r requirements.txt
```

Pick a template and go:

```bash
cd templates/fastapi-llm
uvicorn main:app --reload
```

---

## 🛠️ Prompts

### System Prompts
Ready-to-use system prompts for common use cases:
- [Code Review Assistant](./prompts/system/code-review.md)
- [Technical Writer](./prompts/system/technical-writer.md)
- [Data Analyst](./prompts/system/data-analyst.md)
- [Customer Support Bot](./prompts/system/customer-support.md)

### Few-Shot Templates
- [Classification](./prompts/few-shot/classification.md)
- [Entity Extraction](./prompts/few-shot/entity-extraction.md)
- [Summarization](./prompts/few-shot/summarization.md)

### Chain-of-Thought
- [Math Reasoning](./prompts/chain-of-thought/math-reasoning.md)
- [Step-by-step Debugging](./prompts/chain-of-thought/debugging.md)

---

## 🏗️ Patterns

### RAG (Retrieval Augmented Generation)
```
patterns/rag/
├── basic-rag.py          # Simple vector search + LLM
├── advanced-rag.py       # Reranking + hybrid search
└── README.md
```

### Agents
```
patterns/agents/
├── tool-calling-agent.py   # Function calling pattern
├── react-agent.py          # ReAct (Reason + Act) loop
└── README.md
```

### Chains
```
patterns/chains/
├── summarize-chain.py     # Map-reduce summarization
├── extraction-chain.py    # Structured output extraction
└── README.md
```

---

## ⚡ Templates

### 1. FastAPI LLM API
Production-ready REST API with streaming support.

```
templates/fastapi-llm/
├── main.py           # FastAPI app with /chat endpoint
├── llm.py            # LLM client wrapper
├── models.py         # Pydantic request/response models
├── requirements.txt
└── .env.example
```

**Features:**
- ✅ Streaming responses (SSE)
- ✅ Conversation history management
- ✅ API key auth middleware
- ✅ Rate limiting
- ✅ Docker ready

### 2. LangChain Starter
```
templates/langchain-starter/
├── app.py
├── chains/
├── tools/
└── requirements.txt
```

### 3. Streaming API
Real-time token streaming with FastAPI + React frontend.

---

## 📚 Resources

### Must-Read Papers
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — The transformer paper
- [RAG Paper](https://arxiv.org/abs/2005.11401) — Retrieval-Augmented Generation
- [ReAct](https://arxiv.org/abs/2210.03629) — Reasoning + Acting in LLMs
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903)
- [Constitutional AI](https://arxiv.org/abs/2212.08073) — Anthropic

### Top Tools
| Tool | Use Case |
|------|----------|
| [LangChain](https://langchain.com) | LLM orchestration |
| [LlamaIndex](https://llamaindex.ai) | RAG pipelines |
| [Chroma](https://trychroma.com) | Vector database |
| [Instructor](https://jxnl.github.io/instructor/) | Structured outputs |
| [Outlines](https://github.com/outlines-dev/outlines) | Guided generation |
| [DSPy](https://github.com/stanfordnlp/dspy) | Programmatic prompting |
| [Weave](https://wandb.ai/site/weave) | LLM evaluation & tracing |

### Free Courses
- [Fast.ai Practical Deep Learning](https://course.fast.ai)
- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai)
- [Andrej Karpathy's Zero to Hero](https://karpathy.ai/zero-to-hero.html)

---

## 💡 Examples

| Project | Description | Stack |
|---------|-------------|-------|
| [Chat with PDF](./examples/chat-with-pdf) | RAG over PDF documents | FastAPI + Chroma + Claude |
| [SQL Agent](./examples/sql-agent) | Natural language to SQL | LangChain + SQLite |
| [Code Reviewer](./examples/code-reviewer) | Automated PR reviews | GitHub Actions + OpenAI |

---

## 🤝 Contributing

Got a pattern, prompt, or resource that saved your life? Add it here!

1. Fork the repo
2. Create your branch (`git checkout -b feature/amazing-pattern`)
3. Commit changes (`git commit -m 'Add amazing pattern'`)
4. Push (`git push origin feature/amazing-pattern`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📊 Roadmap

- [ ] LLM evaluation framework
- [ ] Fine-tuning guides (LoRA, QLoRA)
- [ ] Multi-modal patterns (vision + text)
- [ ] LLM observability & monitoring setup
- [ ] Cost optimization patterns

---

## 🙏 Acknowledgements

Inspired by the work of the open-source AI community. Built by [Ashish Yadav](https://github.com/ashish7802).

---

⭐ **If this saved you time, drop a star — it helps others find it!**
