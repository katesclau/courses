# Claude with the Anthropic API

> Course: [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api)

---

## Progress

| Module | Status |
|--------|--------|
| 1. Accessing Claude with the API | ✅ complete |
| 2. Prompt evaluation | ✅ complete |
| 3. Prompt engineering techniques | ✅ complete |
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
- [x] Response streaming → `004_response_streaming.ipynb`
- [x] Structured data → `005_structured_data.ipynb`
- [x] Structured data exercise → `005_structured_data.ipynb`

### Module 2 – Prompt Evaluation

- [x] A typical eval workflow
- [x] Generating test datasets
- [x] Running the eval
- [x] Model-based grading
- [x] Code-based grading
- [x] Exercise on prompt evals → `006_prompt_evaluation.ipynb` · `006_prompt_evals_fns.ipynb`

### Module 3 – Prompt Engineering Techniques

- [x] Being clear and direct
- [x] Being specific
- [x] Structure with XML tags
- [x] Providing examples
- [x] Exercise on prompting → `007_prompting.ipynb`

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
| `004_response_streaming.ipynb` | 1 | Response streaming |
| `005_structured_data.ipynb` | 1 | Structured data · JSON output with prefill |
| `006_prompt_evaluation.ipynb` | 2 | Prompt evaluation pipeline |
| `006_prompt_evals_fns.ipynb` | 2 | Prompt eval helper functions |
| `007_prompting.ipynb` | 3 | Prompt engineering · Dietician agent eval |

---

## Setup

```bash
pip install anthropic python-dotenv
cp .env.example .env  # add your ANTHROPIC_API_KEY
```
