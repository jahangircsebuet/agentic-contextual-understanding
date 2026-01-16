# tests/test_planner.py
from tasks import planning_task
from agents import planner_agent
from test_conftest import run_single_task
import json

def test_planner_outputs_json(sample_post):
    task = planning_task(planner_agent, sample_post)
    output = run_single_task(planner_agent, task)

    data = json.loads(output)
    assert "run" in data
    assert "confidence" in data
    assert "WHAT" in data["run"]
