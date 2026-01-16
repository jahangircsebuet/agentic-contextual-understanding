# tests/test_what.py
from tasks import what_task
from agents import what_agent
from test_conftest import run_single_task
from tasks import what_task
from crewai import Crew
import json


def test_what_agent_basic(sample_post):
    task = what_task(what_agent, sample_post)
    output = run_single_task(what_agent, task)

    assert isinstance(output, str)
    assert len(output) > 20

    text = output.lower()
    assert "student" in text or "protest" in text
    assert "quota" in text
