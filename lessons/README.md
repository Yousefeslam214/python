# Course roadmap: Python, AI & Automation

**Goal:** understand how software and AI work, build real products with AI, and connect apps so work runs by itself. One example is a backend that auto-publishes to LinkedIn.

---

## How the course works

- **Overview first.** In Sessions 2–4 you learn what each tool is, where it lives in a project, and how to read it.
- **Then AI builds.** From Session 4, Claude Code writes the code. You write the plan (the spec), read every change (the diff), run it, and decide: keep it or undo it.
- **Every session:** Part A + Part B, then a **mini-project** and a **quick check**.
- **One demo app:** in class we build a "posts manager" (a Django backend + a React screen). Later it auto-publishes to LinkedIn.
- **Your portfolio:** your mini-projects go into your own GitHub repo, `my-projects`.

> Each session's files appear here about one week before the class.

---

## Phase 1: Sessions 1–7

| # | Part A | Part B | Mini-project |
|---|---|---|---|
| 1 ✔ | Python basics ([`main.py`](../main.py)) | Git + GitHub ([guide](session_1_git_github.md)) | — |
| 2 | Python toolkit ([`lesson_3_toolkit.py`](../lesson_3_toolkit.py)) | SQL + SQL vs NoSQL ([guide](session_2_sql.md)) | Order report |
| 3 | Django overview | Product thinking, prompting, specs | Request-flow map + a product spec |
| 4 | React overview | Claude Code builds your spec | Data trace + your feature, built with AI |
| 5 | AI inside the app (Claude API) | Extending AI: MCP, RAG, local AI | One AI feature |
| 6 | Automation with code: schedule, LinkedIn, deploy | Automation with n8n | Auto-publish + runbook |
| 7 | Capstone (final project) | Growth: SEO, GEO, analytics · handover | Final assessment |

---

## Session by session

### Session 2: Python toolkit + SQL
- **You learn:** functions, imports, files, CSV, JSON, classes, pip · tables, `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, SQL vs NoSQL
- **Mini-project:** Order report: CSV → JSON with Python, plus 3 SQL questions
- **Go deeper:** [roadmap.sh/python](https://roadmap.sh/python) · [roadmap.sh/sql](https://roadmap.sh/sql)

### Session 3: Django overview + product thinking
- **You learn:** what a framework is, how a web request travels, models = tables, the admin, JSON APIs · problem → MVP → spec, and how to prompt AI well
- **Mini-project:** map one page's request flow, write a 1-page product spec, improve one prompt
- **Before this session:** `pip install` works on your laptop (Session 2)
- **Go deeper:** [roadmap.sh/django](https://roadmap.sh/django) · [roadmap.sh/product-manager](https://roadmap.sh/product-manager) · [roadmap.sh/ai-agents](https://roadmap.sh/ai-agents) (the prompting part)

### Session 4: React overview + Claude Code
- **You learn:** frontend vs backend, components, props, state, how React gets data from Django, AI app builders · Claude Code: CLAUDE.md, plan mode, reviewing diffs, tests, keeping secrets in `.env`
- **Mini-project:** trace one post from the database to the screen, then build your own spec with Claude Code
- **Before this session:** Node.js (LTS) installed · Claude Code installed and logged in
- **Go deeper:** [roadmap.sh/react](https://roadmap.sh/react) · [roadmap.sh/claude-code](https://roadmap.sh/claude-code) · [roadmap.sh/vibe-coding](https://roadmap.sh/vibe-coding) · [roadmap.sh/ai-product-builder](https://roadmap.sh/ai-product-builder)

### Session 5: AI inside the app + extending AI
- **You learn:** the Claude API, JSON answers, tool calling, agents and evals (testing AI answers), security · MCP (tools for AI), RAG (AI + your documents), local AI with Hermes
- **Mini-project:** one AI feature with 3 test cases, its cost, and a cloud-vs-local note
- **Before this session:** an Anthropic API key with a spending limit · Hermes + a local model (a big download, so start early)
- **Go deeper:** [roadmap.sh/ai-agents](https://roadmap.sh/ai-agents)

### Session 6: Automate and ship
- **You learn:** scheduled jobs, logs, a kill switch · OAuth and the LinkedIn API · where automation runs, and deployment · n8n workflows with an approval step · AI that runs on a schedule
- **Mini-project:** auto-publish to LinkedIn (dry-run first, then one real post) + a runbook
- **Before this session:** a LinkedIn Page + developer app (start after Session 3, because approval can take time) · n8n · a Telegram bot
- **Go deeper:** [roadmap.sh/claude-code](https://roadmap.sh/claude-code) · [roadmap.sh/ai-product-builder](https://roadmap.sh/ai-product-builder)

### Session 7: Capstone + growth
- **You do:** the final project on a starter app (steps 1–4 at home, steps 5–9 in class)
- **You learn:** SEO, GEO (being found by AI search), analytics, user feedback
- **Go deeper:** [roadmap.sh/seo](https://roadmap.sh/seo) · [roadmap.sh/product-manager](https://roadmap.sh/product-manager)

---

## How you are assessed (Session 7)

| Skill | Weight |
|---|---|
| Read and explain code | 20% |
| Debug from errors and logs | 15% |
| Safe Git/GitHub work | 15% |
| SQL and data | 15% |
| Prompting + AI APIs | 15% |
| Security and review | 10% |
| Automation readiness | 10% |

---

## Phase 2: Sessions 8–12 (deep dives)

Turn the posts manager into a real, launched product.

| # | Deep dive | Mini-project | Go deeper |
|---|---|---|---|
| 8 | Django + databases: REST API, users and permissions, tests, PostgreSQL, MongoDB | Per-user posts with tests, on PostgreSQL | [django](https://roadmap.sh/django) |
| 9 | React: pages, forms, login, Tailwind, TypeScript and Next.js overview | Login + dashboard + post form | [react](https://roadmap.sh/react) |
| 10 | Production: Docker, GitHub Actions, deploy, domain, monitoring | Push → tests → deploy; auto-publish runs without your laptop | [ai-product-builder](https://roadmap.sh/ai-product-builder) |
| 11 | AI agents: your own MCP server, agent frameworks, evals, tracing, guardrails | MCP server + one agent with 10 test cases | [ai-agents](https://roadmap.sh/ai-agents) · [claude-code](https://roadmap.sh/claude-code) |
| 12 | Grow and launch: SEO + GEO in depth, product management, analytics, A/B tests | Landing page + analytics + launch plan | [seo](https://roadmap.sh/seo) · [product-manager](https://roadmap.sh/product-manager) |

---

## Optional: computer science

Want to know how computers work underneath (data structures, algorithms, networks)? Study it at your own pace: [roadmap.sh/computer-science](https://roadmap.sh/computer-science).
