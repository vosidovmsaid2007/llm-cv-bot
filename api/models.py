from pydantic import BaseModel
from typing import List

class ResumeRequest(BaseModel):
    text: str

class SkillsResponse(BaseModel):
    skills: List[str]