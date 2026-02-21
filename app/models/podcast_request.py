from pydantic import BaseModel


class PodcastRequest(BaseModel):
    text_input: str
