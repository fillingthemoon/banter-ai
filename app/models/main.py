from pydantic import BaseModel
from typing import List, Literal

class DialogueLine(BaseModel):
    speaker: Literal["host", "guest"]
    text: str


class PodcastScript(BaseModel):
    title: str
    content: List[DialogueLine]
