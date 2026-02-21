from typing import Optional

from pydantic import BaseModel

from app.models.main import PodcastScript
from app.models.status import JobStatus


class Job(BaseModel):
    id: str
    status: JobStatus
    text_input: str
    result: Optional[PodcastScript]
    error: Optional[str]
    url: str | None
