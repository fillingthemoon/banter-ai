from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.models.job_manager import JobManager, job_manager
from app.models.job import Job
from app.models.job_receipt import JobReceipt
from app.services.main import process_podcast

router = APIRouter()


@router.post("/generate-podcast", response_model=JobReceipt)
async def start_podcast_gen(text_input: str, background_tasks: BackgroundTasks):
    new_job = JobManager.create_job(text_input)

    job_manager.add_job(new_job)

    background_tasks.add_task(process_podcast, new_job.id, text_input)

    job_receipt = JobReceipt(
        job_id=new_job.id,
        status=new_job.status,
        message=f"Podcast generation for job with id '{new_job.id}' started!",
    )

    return job_receipt


@router.get("/status/{job_id}", response_model=Job)
async def get_status(job_id: str):
    job = job_manager.get_job(job_id)

    if not job:
        raise HTTPException(status_code=404, detail=f"Job with id '{job_id}' not found")

    return job
