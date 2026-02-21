import logging

logger = logging.getLogger(__name__)


def process_podcast(job_id: str, text_input: str):
    logger.info(f"Processing podcast job {job_id} with input {text_input}...")
    logger.info("Successfully processed podcast job {job_id} with input {text_input}.")
