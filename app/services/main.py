from datetime import datetime
import json
import os
import logging

from openai import OpenAI

from app.models.job_manager import job_manager
from app.models.result import PodcastScript
from dotenv import load_dotenv

from app.services.audio_generator import audio_generator
from app.services.utils import MODEL, SYSTEM_PROMPT

logger = logging.getLogger(__name__)

load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1", api_key=os.getenv("GROQ_API_KEY")
)


class PodcastProcessor:
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

        logger.info(f"Raw response content: {content}")

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

    def process_podcast(self, job_id: str, text_input: str):
        logger.info(
            f"Processing podcast job with id '{job_id}' and text input '{text_input}'..."
        )

        script = self.generate_script(job_id, text_input)

        self.export_script(script)

        # audio_generator.generate_audio(job_id, script)

        job = job_manager.get_job(job_id)

        if not job:
            raise Exception(f"Job with id {job_id} not found.")

        job.mark_complete(script)

        logger.info(
            f"Successfully processed podcast job with id '{job_id}' and text input '{text_input}'."
        )


podcast_processor = PodcastProcessor()
