# tests/test_how.py
from tasks import how_task
from agents import how_agent
from test_conftest import run_single_task

def test_how_agent_sentiment(sample_engagement_context):
    task = how_task(how_agent, sample_engagement_context)
    output = run_single_task(how_agent, task)

    text = output.lower()
    assert "sentiment" in text or "reaction" in text
    assert "supportive" in text or "angry" in text
