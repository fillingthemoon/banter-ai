import json
import os
import logging

from openai import OpenAI

from app.models.job_manager import job_manager
from app.models.result import PodcastScript
from dotenv import load_dotenv

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

    def generate_audio(self, job_id: str):
        logger.info(f"Generating audio for job with id '{job_id}'...")
        # audio_segments = []

        # for _, line in enumerate(script.content):
        #     voice_id = (
        #         "ALEX_VOICE_ID" if line.speaker.lower() == "alex" else "SAM_VOICE_ID"
        #     )

        #     audio = generate_audio_for_line(line.text, voice_id)
        #     audio_segments.append(audio)

        # final_audio = sum(audio_segments)
        # final_audio.export(f"podcasts/{job_id}.mp3", format="mp3")

        logger.info(f"Successfully generated audio for job with id '{job_id}'.")

    def process_podcast(self, job_id: str, text_input: str):
        logger.info(
            f"Processing podcast job with id '{job_id}' and text input '{text_input}'..."
        )

        script = self.generate_script(job_id, text_input)

        self.generate_audio(job_id)

        job = job_manager.get_job(job_id)

        if not job:
            raise Exception(f"Job with id {job_id} not found.")

        job.mark_complete(script)

        logger.info(
            f"Successfully processed podcast job with id '{job_id}' and text input '{text_input}'."
        )


podcast_processor = PodcastProcessor()
