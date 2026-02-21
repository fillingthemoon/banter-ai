from typing import Optional

from pydantic import BaseModel

from app.models.result import PodcastScript
from app.models.status import JobStatus


class Job(BaseModel):
    id: str
    status: JobStatus
    text_input: str
    result: Optional[PodcastScript]
    error: Optional[str]
    url: Optional[str]

    def mark_complete(self, script: PodcastScript):
        self.status = "completed"
        self.result = script

    def mark_failed(self, error_message: str):
        self.status = "failed"
        self.error = error_message
