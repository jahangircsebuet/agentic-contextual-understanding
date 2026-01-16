# tests/test_when.py
from tasks import when_task
from agents import when_agent
from test_conftest import run_single_task

def test_when_agent_temporal(sample_temporal_context):
    task = when_task(when_agent, sample_temporal_context)
    output = run_single_task(when_agent, task)

    text = output.lower()
    assert "2025" in text or "december" in text
    assert "student" in text or "protest" in text

# No guessing test
def test_when_agent_no_fabrication(sample_temporal_context):
    task = when_task(when_agent, sample_temporal_context)
    output = run_single_task(when_agent, task)

    assert "definitely" not in output.lower()
    assert "confirmed" not in output.lower()
