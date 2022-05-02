from typing import Dict, List
from pydantic import BaseModel


class TextInput(BaseModel):
    """
    Input text value
    """
    text: str


class TaskClassScore(BaseModel):
    """
    Input text value
    """
    class_value: str
    score: float


class TaskClassesScore(BaseModel):
    task_id: int
    scores: List[TaskClassScore]


class ModelResponse(BaseModel):
    response: List[TaskClassesScore]
