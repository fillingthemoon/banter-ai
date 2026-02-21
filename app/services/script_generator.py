from datetime import datetime
import io
import json
import logging
import os
from dotenv import load_dotenv
from openai import OpenAI

from app.models.result import PodcastScript
from app.services.utils import MODEL, SYSTEM_PROMPT

logger = logging.getLogger(__name__)

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1", api_key=os.getenv("GROQ_API_KEY")
)


class ScriptGenerator:
    def generate_script(self, job_id: str, topic: str) -> PodcastScript:
        logger.info(f"Generating script for job with id '{job_id}'...")

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {"role": "user", "content": f"Topic: {topic}"},
            ],
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content

        if not content:
            raise Exception(f"Response for job with id {job_id} is None.")
        else:
            validated_content = PodcastScript.model_validate_json(content)
            logger.info(f"Successfully generated script for job with id '{job_id}'.")
            return validated_content

    def export_script(self, script: PodcastScript):
        path = "podcasts/scripts"
        os.makedirs(path, exist_ok=True)

        script_dict = script.model_dump(mode="json")

        filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        file_path = os.path.join("podcasts/scripts", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(script_dict, f, indent=4)


script_generator = ScriptGenerator()
