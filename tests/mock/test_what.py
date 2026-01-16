# tests/test_what.py
from tasks import what_task
from agents import what_agent
from conftest import run_single_task
from tasks import what_task
from crewai import Crew
import json


# for mock test 
def test_what_agent_basic(mock_agents, sample_post):
    agent = mock_agents["what"]
    task = what_task(agent, sample_post)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    output = crew.kickoff()

    parsed = json.loads(output.raw)

    assert "summary" in parsed
    assert "themes" in parsed
    assert isinstance(parsed["themes"], list)
