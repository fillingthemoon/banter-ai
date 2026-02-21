import uuid

from app.models.job import Job


class JobManager:
    def __init__(self) -> None:
        self._jobs: dict[str, Job] = {}

    def add_job(self, job: Job) -> None:
        self._jobs[job.id] = job

    def get_job(self, job_id: str) -> Job | None:
        return self._jobs.get(job_id, None)

    @staticmethod
    def create_job(text_input: str) -> Job:
        return Job(
            id=str(uuid.uuid4()),
            status="processing",
            text_input=text_input,
            result=None,
            error=None,
            url=None,
        )


job_manager = JobManager()
