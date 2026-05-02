# 📚 LLM Resources

Curated list of the best resources for LLM engineers.

---

## 📄 Must-Read Papers

| Paper | Why It Matters |
|-------|---------------|
| [Attention Is All You Need (2017)](https://arxiv.org/abs/1706.03762) | The original transformer — everything starts here |
| [GPT-3 (2020)](https://arxiv.org/abs/2005.14165) | Few-shot learning with large models |
| [RAG (2020)](https://arxiv.org/abs/2005.11401) | Retrieval-Augmented Generation pattern |
| [Chain-of-Thought (2022)](https://arxiv.org/abs/2201.11903) | Step-by-step reasoning prompting |
| [ReAct (2022)](https://arxiv.org/abs/2210.03629) | Reasoning + Acting with tools |
| [Constitutional AI (2022)](https://arxiv.org/abs/2212.08073) | Anthropic's alignment approach |
| [Toolformer (2023)](https://arxiv.org/abs/2302.04761) | Teaching LLMs to use APIs |
| [Self-RAG (2023)](https://arxiv.org/abs/2310.11511) | LLM decides when to retrieve |
| [Mixture of Experts (2024)](https://arxiv.org/abs/2401.04088) | Efficient scaling with MoE |

---

## 🛠️ Tools & Frameworks

### Orchestration
| Tool | Use Case | Stars |
|------|----------|-------|
| [LangChain](https://github.com/langchain-ai/langchain) | Full LLM app framework | 90k+ |
| [LlamaIndex](https://github.com/run-llama/llama_index) | RAG & data connectors | 35k+ |
| [DSPy](https://github.com/stanfordnlp/dspy) | Programmatic prompting | 17k+ |
| [Haystack](https://github.com/deepset-ai/haystack) | NLP pipelines | 15k+ |

### Vector Databases
| Tool | Best For |
|------|----------|
| [ChromaDB](https://github.com/chroma-core/chroma) | Local/simple projects |
| [Pinecone](https://pinecone.io) | Production scale |
| [Weaviate](https://weaviate.io) | GraphQL + vector |
| [Qdrant](https://qdrant.tech) | High performance |
| [pgvector](https://github.com/pgvector/pgvector) | PostgreSQL integration |

### Structured Outputs
| Tool | What It Does |
|------|-------------|
| [Instructor](https://github.com/jxnl/instructor) | Pydantic-based structured output |
| [Outlines](https://github.com/outlines-dev/outlines) | Regex/JSON guided generation |
| [Marvin](https://github.com/PrefectHQ/marvin) | AI functions with type hints |

### Observability & Eval
| Tool | What It Does |
|------|-------------|
| [LangSmith](https://smith.langchain.com) | Tracing & evaluation |
| [Weave (W&B)](https://wandb.ai/site/weave) | LLM experiment tracking |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt testing & red-teaming |
| [RAGAS](https://github.com/explodinggradients/ragas) | RAG pipeline evaluation |

---

## 🎓 Free Courses

| Course | Provider | Level |
|--------|----------|-------|
| [Practical Deep Learning](https://course.fast.ai) | fast.ai | Beginner → Advanced |
| [LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | FSDL | Intermediate |
| [Building Systems with ChatGPT](https://learn.deeplearning.ai) | DeepLearning.AI | Beginner |
| [LangChain for LLM Apps](https://learn.deeplearning.ai) | DeepLearning.AI | Beginner |
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Andrej Karpathy | Intermediate |
| [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) | HuggingFace | Beginner |

---

## 🌐 Best Blogs & Newsletters

- [Lilian Weng's Blog](https://lilianweng.github.io) — Deep technical posts from OpenAI
- [Sebastian Raschka](https://magazine.sebastianraschka.com) — ML research explained
- [The Batch (Andrew Ng)](https://www.deeplearning.ai/the-batch/) — Weekly AI news
- [Ahead of AI](https://magazine.sebastianraschka.com) — LLM research digest
- [Eugene Yan](https://eugeneyan.com) — Applied ML in industry

---

## 🤖 LLM APIs

| Provider | Models | Free Tier |
|----------|--------|-----------|
| [Anthropic](https://anthropic.com) | Claude 3.5 Sonnet/Haiku | Yes |
| [OpenAI](https://platform.openai.com) | GPT-4o, o1 | No (credits) |
| [Google](https://ai.google.dev) | Gemini 2.0 | Yes |
| [Groq](https://groq.com) | Llama, Mixtral | Yes (fast!) |
| [Together AI](https://together.ai) | 50+ open models | Yes |
| [Ollama](https://ollama.ai) | Local models | Free (local) |
