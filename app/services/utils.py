import json

from app.models.result import PodcastScript


SCHEMA_INSTRUCTIONS = json.dumps(PodcastScript.model_json_schema(), indent=2)

SYSTEM_PROMPT = f"""
You are a professional podcast script writer. 
You MUST return a JSON object that matches this EXACT schema structure:

{SCHEMA_INSTRUCTIONS}

CRITICAL RULES:
1. Use the key "title" for the podcast name.
2. Use the key "content" for the list of dialogue.
3. Each item in "content" must have "speaker" and "text" (NOT "dialog").
4. Do not include any text, greetings, or explanations outside the JSON.
"""

MODEL = "llama-3.3-70b-versatile"
