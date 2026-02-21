from pydantic import BaseModel
from typing import List, Literal


class DialogueLine(BaseModel):
    speaker: Literal["host", "guest"]
    text: str
    emotion: Literal["excited", "skeptical", "laughing"]


class PodcastScript(BaseModel):
    title: str
    content: List[DialogueLine]
