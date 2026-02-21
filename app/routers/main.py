from fastapi import APIRouter, BackgroundTasks
import uuid

from app.services.main import process_podcast

router = APIRouter()

jobs = {}


@router.post("/generate-podcast")
async def start_podcast_gen(text_input: str, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "processing", "url": None}

    background_tasks.add_task(process_podcast, job_id, text_input)

    return {"job_id": job_id, "message": "Podcast generation started!"}


@router.get("/status/{job_id}")
async def get_status(job_id: str):
    return jobs.get(job_id, {"status": "not_found"})
