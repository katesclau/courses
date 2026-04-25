# Claude with the Anthropic API

> Course: [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)

---

## Progress

| Module | Status |
|--------|--------|
| 1. Accessing Claude with the API | 🔄 in progress (Temperature) |
| 2. Prompt evaluation | ⬜ pending |
| 3. Prompt engineering techniques | ⬜ pending |
| 4. Tool use with Claude | ⬜ pending |
| 5. RAG and Agentic Search | ⬜ pending |
| 6. Features of Claude | ⬜ pending |
| 7. Model Context Protocol | ⬜ pending |
| 8. Anthropic Apps – Claude Code & Computer Use | ⬜ pending |
| 9. Agents and Workflows | ⬜ pending |

---

## Curriculum

### Module 1 – Accessing Claude with the API

- [x] Overview of Claude models
- [x] Getting an API key
- [x] Making a request
- [x] Multi-turn conversations
- [x] Chat exercise → `001_requests.ipynb`
- [x] System prompts
- [x] System prompts exercise → `002_system_prompts.ipynb`
- [x] Temperature → `003_temperature.ipynb`
- [ ] Response streaming
- [ ] Structured data
- [ ] Structured data exercise

### Module 2 – Prompt Evaluation

- [ ] A typical eval workflow
- [ ] Generating test datasets
- [ ] Running the eval
- [ ] Model-based grading
- [ ] Code-based grading
- [ ] Exercise on prompt evals

### Module 3 – Prompt Engineering Techniques

- [ ] Being clear and direct
- [ ] Being specific
- [ ] Structure with XML tags
- [ ] Providing examples
- [ ] Exercise on prompting

### Module 4 – Tool Use with Claude

- [ ] Tool functions
- [ ] Tool schemas
- [ ] Handling message blocks
- [ ] Sending tool results
- [ ] Multi-turn conversations with tools
- [ ] Using multiple tools
- [ ] Fine-grained tool calling
- [ ] The text edit tool
- [ ] The web search tool

### Module 5 – RAG and Agentic Search

- [ ] Text chunking strategies
- [ ] Text embeddings
- [ ] The full RAG flow
- [ ] BM25 lexical search
- [ ] A multi-index RAG pipeline

### Module 6 – Features of Claude

- [ ] Extended thinking
- [ ] Image support
- [ ] PDF support
- [ ] Citations
- [ ] Prompt caching
- [ ] Code execution and the Files API

### Module 7 – Model Context Protocol (MCP)

- [ ] MCP clients
- [ ] Project setup
- [ ] Defining tools with MCP
- [ ] The server inspector
- [ ] Implementing a client
- [ ] Defining resources & prompts

### Module 8 – Anthropic Apps

- [ ] Claude Code setup
- [ ] Claude Code in action
- [ ] Enhancements with MCP servers

### Module 9 – Agents and Workflows

- [ ] Parallelization workflows
- [ ] Chaining workflows
- [ ] Routing workflows
- [ ] Agents and tools
- [ ] Workflows vs agents

---

## Notebooks

| File | Module | Topic |
|------|--------|-------|
| `001_requests.ipynb` | 1 | Making requests · Multi-turn chat |
| `002_system_prompts.ipynb` | 1 | System prompts · Output format control |
| `003_temperature.ipynb` | 1 | Temperature · Brainstorming with system prompts |

---

## Setup

```bash
pip install anthropic python-dotenv
cp .env.example .env  # add your ANTHROPIC_API_KEY
```
