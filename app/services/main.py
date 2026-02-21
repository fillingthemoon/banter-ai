import logging
import time

from app.models.job_manager import job_manager
from app.models.result import DialogueLine, PodcastScript

logger = logging.getLogger(__name__)


def process_podcast(job_id: str, text_input: str):
    logger.info(
        f"Processing podcast job with id '{job_id}' and text input '{text_input}'..."
    )

    time.sleep(10)

    result_script = PodcastScript(
        title="Script 1",
        content=[
            DialogueLine(speaker="host", text="line 1"),
            DialogueLine(speaker="guest", text="line 2"),
            DialogueLine(speaker="host", text="line 3"),
            DialogueLine(speaker="guest", text="line 4"),
        ],
    )

    job = job_manager.get_job(job_id)

    if not job:
        raise Exception(f"Job with id {job_id} not found.")

    job.mark_complete(result_script)

    logger.info(
        f"Successfully processed podcast job with id '{job_id}' and text input '{text_input}'."
    )
