# ActionAgent

ActionAgent is an MVP AI assistant for students that plans tasks, helps with research, and integrates with Google tools while preserving academic integrity.

## What’s included

- FastAPI backend with task planning, quiz generation, and Google OAuth placeholders
- React + Tailwind frontend for prompt-driven student workflows
- Structured docs and integrity guidance for a student-focused MVP

## Setup

### Backend

1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\Activate.ps1`
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and set keys
6. `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

### Frontend

1. `cd frontend`
2. `npm install`
3. `npm run dev`

## Example prompts

- "Turn this syllabus into a week-long study plan with daily work blocks."
- "Generate a 20-question quiz from these lecture notes and schedule a review tomorrow."
- "Find 5 academic sources on quantum entanglement and summarize each in three bullets."

## Academic integrity

ActionAgent is designed as a study aid, not a cheating tool. It should:

- summarize sources with citations
- never generate a complete essay without review
- offer concept explanations at multiple levels
- prompt the student to verify submissions manually

## MVP focus

- Google Calendar + Google Docs integration placeholders
- assignment planning and study scheduling
- quiz generation from notes/PDF summaries
