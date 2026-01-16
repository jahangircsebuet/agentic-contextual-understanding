# tests/test_where.py
from tasks import where_task
from agents import where_agent
from test_conftest import run_single_task

def test_where_agent_context(sample_surface_context):
    task = where_task(where_agent, sample_surface_context)
    output = run_single_task(where_agent, task)

    text = output.lower()
    assert "group" in text
    assert "students" in text or "audience" in text
