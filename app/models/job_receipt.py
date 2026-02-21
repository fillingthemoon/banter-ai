from pydantic import BaseModel

from app.models.status import JobStatus


class JobReceipt(BaseModel):
    job_id: str
    status: JobStatus
    message: str
