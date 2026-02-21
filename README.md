# Banter AI

Transform a long-form blog post or a research paper into a two-person podcast script with realistic, emotive voices!

## Tech stack

- FastAPI
- OpenAI
- Groq
- ElevenLabs
- Pydub

## Local development

1. Install `uv`.

```bash
brew install uv
```

2. Set the `Python: Select Interpreter` to `.venv/bin/python`.

3. Create `.vscode/launch.json`.

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

5. Navigate to the FastAPI Swagger interface and try these sample prompts.

> The Sun is a dynamic G-type main-sequence star at the center of our solar system, accounting for 99.8% of its total mass. Powered by nuclear fusion in its core, it converts hydrogen into helium, releasing the energy that sustains life on Earth. Its structure consists of several layers: the core, radiative zone, convective zone, and the visible surface known as the photosphere. Above this lies the solar atmosphere, including the corona, which mysteriously burns much hotter than the surface. Through the solar wind and magnetic activity—like sunspots and flares—the Sun dictates space weather, influencing satellite communications and auroras. Despite its stability, it is roughly halfway through its 10-billion-year life cycle before it will eventually evolve into a red giant.
