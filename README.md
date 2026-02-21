# Banter AI

Transform a long-form blog post or a research paper into a two-person podcast script with realistic, emotive voices!

## Features

-

## Tech stack

- Fast API
- Pydantic
- Docker

## Local development

1. Install `uv`.

```bash
brew install uv
```

2. Set the `Python: Select Interpreter` to `.venv/bin/python`.

3. Create `.vscode/launch.json`

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI via uv",
      "type": "debugpy",
      "request": "launch",
      "module": "fastapi",
      "args": ["dev", "app/main.py"],
      "python": "${command:python.interpreterPath}"
    }
  ]
}
```

4. Run debugger.
