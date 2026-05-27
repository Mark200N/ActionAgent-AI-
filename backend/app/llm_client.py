import os
from typing import Any, Dict
import httpx

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

async def llm_chain(agent_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Placeholder LLM wrapper for assignment planning and summarization."""
    if not OPENAI_API_KEY:
        return {
            "schedule": [],
            "notes": "OpenAI API key is not configured.",
            "warnings": ["Configure OPENAI_API_KEY in backend/.env"],
        }

    prompt = build_prompt(agent_name, payload)
    response = await call_openai(prompt)
    return parse_response(agent_name, response)

def build_prompt(agent_name: str, payload: Dict[str, Any]) -> str:
    if agent_name == "assignment_planner":
        return (
            "You are a student planning assistant. Split the assignment into daily tasks, "
            "estimate time blocks, and create a study schedule around classes. Use the input prompt and "
            "the optional syllabus text and deadline. Return a JSON list of days, tasks, and minutes.\n\n"
            f"{payload}\n"
        )

    if agent_name == "quiz_generator":
        return (
            "You are a quiz builder. Create a set of study questions based on the user's notes or prompt. "
            "Return a JSON array of questions with short answers and optional multiple-choice options.\n\n"
            f"{payload}\n"
        )

    if agent_name == "source_summarizer":
        return (
            "You are an academic research assistant. Find scholarly sources, summarize each in three bullets, "
            "and include a citation. Return a JSON array of titles, citations, summaries, and URLs.\n\n"
            f"{payload}\n"
        )

    return f"Agent: {agent_name}\nPayload: {payload}"

async def call_openai(prompt: str) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 700,
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            f"{OPENAI_API_BASE}/chat/completions",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        return response.json()


def parse_response(agent_name: str, response: Dict[str, Any]) -> Dict[str, Any]:
    if not response:
        return {}
    content = response.get("choices", [])[0].get("message", {}).get("content", "")

    # Minimal fallback parsing for the MVP. Workflows should be improved with function calling.
    if agent_name == "assignment_planner":
        return {"schedule": [{"day": "TBD", "tasks": [content], "estimated_minutes": 30}], "notes": content}
    if agent_name == "quiz_generator":
        return {"questions": [{"question": content, "answer": "See explanation notes."}], "notes": content}
    if agent_name == "source_summarizer":
        return {"sources": [{"title": "Source summary", "citation": "TBD", "summary": [content], "url": None}], "notes": content}
    return {"notes": content}
