from fastapi import FastAPI, Body
from api.models import ResumeRequest, SkillsResponse
import config

app = FastAPI(title="Resume Skills Extractor API")

@app.post("/extract_skills", response_model=SkillsResponse)
def extract_skills(data: ResumeRequest = Body(...)):
    text_lower = data.text.lower()
    found = [skill for skill in config.SKILLS if skill.lower() in text_lower]
    return SkillsResponse(skills=found)
