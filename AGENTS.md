# Repository Guidelines

## Project Structure & Module Organization
- `main.py` is the entrypoint and defines the LangChain agent wiring: `ChatOllama` LLM, `TavilySearch` tool, and Pydantic response models (`AgentResponse`, `Source`).
- `pyproject.toml` declares Python 3.12+, core dependencies, and formatter/linter tools; `uv.lock` tracks the exact resolved set for reproducible installs.
- `.env` (gitignored) loads API keys at startup; keep local copies only. `.venv/` is the recommended virtual environment location.
- `README.md` is currently a placeholder; prefer adding runnable examples there when you extend the agent.

## Setup, Build, and Run
- Install dependencies with `uv sync` (preferred; uses `uv.lock`). If you do not have uv, install it first (`pip install uv` or the installer at astral.sh).
- Run the agent: `uv run python main.py`. Ensure your `.env` contains `TAVILY_API_KEY` and the local Ollama model referenced in `ChatOllama` is available.
- Format and import-sort before pushing: `uv run black main.py` and `uv run isort main.py`.
- If you introduce additional scripts, add a short comment near the command in `README.md` so others can reproduce quickly.

## Coding Style & Naming Conventions
- Follow Black defaults (4-space indentation, 88-character lines) and isort’s default profile.
- Use type hints throughout; keep Pydantic models concise with docstrings for schema clarity.
- Functions and tools use `snake_case`; classes use `PascalCase`; constants in `UPPER_SNAKE_CASE`.
- Keep tool definitions small and composable; prefer one clear responsibility per tool.

## Testing Guidelines
- No automated tests exist yet; new features should add `pytest` cases under `tests/` (e.g., `tests/test_main.py`).
- For tools that call external services, add thin fakes or environment-guarded integration tests; document required keys in the test file header.
- Run tests with `uv run pytest` once added, and note pass/fail status in your PR description.

## Commit & Pull Request Guidelines
- Git history favors short, imperative summaries (e.g., `search agent`, `Update main.py`); keep subject lines under ~72 characters.
- In pull requests, include: goal/impact summary, manual commands run (e.g., `uv run python main.py`, formatters, tests), and any configuration steps (`.env` keys, local model choices).
- Attach screenshots or log snippets only when they clarify behavior; avoid pasting secrets or full tracebacks that reveal tokens.

## Security & Configuration Tips
- Never commit `.env` or credentials; rely on `python-dotenv` loading locally.
- Validate that the Ollama model name in `ChatOllama` matches what you have pulled; avoid hard-coding personal URLs or ports.
- When adding new tools, sanitize outputs and avoid echoing sensitive query parameters in logs.
