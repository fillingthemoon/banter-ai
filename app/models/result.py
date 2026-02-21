from pydantic import BaseModel
from typing import Literal


class DialogueLine(BaseModel):
    speaker: Literal["host", "guest"]
    text: str
    emotion: Literal["excited", "skeptical", "laughing"]


class PodcastScript(BaseModel):
    title: str
    content: list[DialogueLine]
