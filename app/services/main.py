import logging

from app.models.job_manager import job_manager

from app.services.script_generator import script_generator

# from app.services.audio_generator import audio_generator

logger = logging.getLogger(__name__)


class PodcastProcessor:
    def process_podcast(self, job_id: str, text_input: str):
        logger.info(f"Processing podcast job with id '{job_id}'...")

        script = script_generator.generate_script(job_id, text_input)
        script_generator.export_script(script)

        # audio_generator.generate_audio(job_id, script)

        job = job_manager.get_job(job_id)

        if not job:
            raise Exception(f"Job with id {job_id} not found.")

        job.mark_complete(script)

        logger.info(f"Successfully processed podcast job with id '{job_id}'.")


podcast_processor = PodcastProcessor()
