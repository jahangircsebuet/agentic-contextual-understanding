# tests/test_who.py
from tasks import who_task
from agents import who_agent
from test_conftest import run_single_task

def test_who_agent_persona(sample_user_context):
    task = who_task(who_agent, sample_user_context)
    output = run_single_task(who_agent, task)

    text = output.lower()
    assert "student" in text or "educator" in text
    assert "history" in text or "posts" in text


# Negative test (important)
def test_who_agent_no_sensitive_attributes(sample_user_context):
    task = who_task(who_agent, sample_user_context)
    output = run_single_task(who_agent, task)

    forbidden = ["religion", "ethnicity", "race"]
    for f in forbidden:
        assert f not in output.lower()
