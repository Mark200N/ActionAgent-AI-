from fastapi import APIRouter, HTTPException, status
from .schemas import (
    AssignmentPlanRequest,
    AssignmentPlanResponse,
    QuizRequest,
    QuizResponse,
    SourceSummaryRequest,
    SourceSummaryResponse,
)
from .llm_client import llm_chain
from .google_oauth import get_google_oauth_url

api_router = APIRouter()

@api_router.post("/tasks/plan", response_model=AssignmentPlanResponse)
async def plan_assignment(request: AssignmentPlanRequest):
    plan = await llm_chain("assignment_planner", request.dict())
    return AssignmentPlanResponse(
        prompt=request.prompt,
        schedule=plan.get("schedule", []),
        notes=plan.get("notes", ""),
        warnings=plan.get("warnings", []),
    )

@api_router.post("/tasks/quiz", response_model=QuizResponse)
async def make_quiz(request: QuizRequest):
    quiz = await llm_chain("quiz_generator", request.dict())
    return QuizResponse(
        prompt=request.prompt,
        questions=quiz.get("questions", []),
        deck_id=quiz.get("deck_id"),
        notes=quiz.get("notes", ""),
    )

@api_router.post("/sources/summarize", response_model=SourceSummaryResponse)
async def summarize_sources(request: SourceSummaryRequest):
    summary = await llm_chain("source_summarizer", request.dict())
    return SourceSummaryResponse(
        prompt=request.prompt,
        sources=summary.get("sources", []),
        notes=summary.get("notes", ""),
    )

@api_router.get("/auth/google")
async def auth_google():
    return {"auth_url": get_google_oauth_url()}

@api_router.get("/health")
async def health_check():
    return {"status": "ok"}
