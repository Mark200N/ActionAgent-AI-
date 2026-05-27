from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class AssignmentPlanRequest(BaseModel):
    prompt: str
    deadline: Optional[date] = None
    available_hours_per_day: Optional[float] = 2.0
    syllabus_text: Optional[str] = None

class PlanItem(BaseModel):
    day: str
    tasks: List[str]
    estimated_minutes: int

class AssignmentPlanResponse(BaseModel):
    prompt: str
    schedule: List[PlanItem]
    notes: Optional[str]
    warnings: List[str] = []

class QuizRequest(BaseModel):
    prompt: str
    notes_text: Optional[str] = None
    target_date: Optional[date] = None
    questions_count: Optional[int] = 20

class QuizQuestion(BaseModel):
    question: str
    choices: Optional[List[str]] = None
    answer: Optional[str] = None

class QuizResponse(BaseModel):
    prompt: str
    questions: List[QuizQuestion]
    deck_id: Optional[str] = None
    notes: Optional[str]

class SourceSummaryRequest(BaseModel):
    prompt: str
    query: Optional[str] = None
    source_urls: Optional[List[str]] = []
    max_sources: Optional[int] = 5

class SourceItem(BaseModel):
    title: str
    citation: str
    summary: List[str]
    url: Optional[str] = None

class SourceSummaryResponse(BaseModel):
    prompt: str
    sources: List[SourceItem]
    notes: Optional[str]
