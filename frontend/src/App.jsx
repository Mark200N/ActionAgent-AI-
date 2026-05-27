import { useState } from 'react';

const API_BASE = 'http://localhost:8000/api';

function App() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState(null);
  const [mode, setMode] = useState('plan');
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    if (!prompt.trim()) return;
    setLoading(true);
    const path = mode === 'quiz' ? 'tasks/quiz' : mode === 'research' ? 'sources/summarize' : 'tasks/plan';
    const body = { prompt, notes_text: prompt };
    try {
      const response = await fetch(`${API_BASE}/${path}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      setResult({ error: error.message });
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <div className="mx-auto max-w-4xl rounded-3xl bg-slate-900/90 p-8 shadow-2xl shadow-slate-900/20">
        <h1 className="mb-4 text-4xl font-semibold text-cyan-300">ActionAgent</h1>
        <p className="mb-6 text-slate-300">Student planning, research and quiz support with Google tool integration in development.</p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <label className="block">
            <span className="text-sm text-slate-400">Task prompt</span>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              rows={5}
              className="mt-2 w-full rounded-2xl border border-slate-700 bg-slate-950 p-4 text-slate-100 outline-none focus:border-cyan-400"
              placeholder="e.g. Turn these 3 lecture PDFs into a 20-question quiz and schedule it for tomorrow"
            />
          </label>

          <div className="flex flex-wrap gap-3">
            <button
              type="button"
              onClick={() => setMode('plan')}
              className={`rounded-full px-4 py-2 ${mode === 'plan' ? 'bg-cyan-500 text-slate-950' : 'bg-slate-800 text-slate-300'}`}
            >
              Plan
            </button>
            <button
              type="button"
              onClick={() => setMode('quiz')}
              className={`rounded-full px-4 py-2 ${mode === 'quiz' ? 'bg-cyan-500 text-slate-950' : 'bg-slate-800 text-slate-300'}`}
            >
              Quiz
            </button>
            <button
              type="button"
              onClick={() => setMode('research')}
              className={`rounded-full px-4 py-2 ${mode === 'research' ? 'bg-cyan-500 text-slate-950' : 'bg-slate-800 text-slate-300'}`}
            >
              Research
            </button>
          </div>

          <button
            type="submit"
            className="rounded-3xl bg-cyan-500 px-6 py-3 font-semibold text-slate-950 transition hover:bg-cyan-400"
            disabled={loading}
          >
            {loading ? 'Working…' : 'Generate'}
          </button>
        </form>

        <div className="mt-8 rounded-3xl border border-slate-800 bg-slate-950/80 p-6">
          <h2 className="text-2xl font-semibold text-slate-100">Results</h2>
          {result ? (
            <pre className="mt-4 overflow-x-auto whitespace-pre-wrap text-sm text-slate-200">{JSON.stringify(result, null, 2)}</pre>
          ) : (
            <p className="mt-4 text-slate-400">Submit a prompt to see the agent produce a plan, quiz, or source summary.</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
