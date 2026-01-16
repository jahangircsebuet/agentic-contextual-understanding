import json
from crewai import Crew
from tasks import planning_task

def test_planner_outputs_valid_route(mock_agents, sample_post):
    agent = mock_agents["planner"]
    task = planning_task(agent, sample_post)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "run" in parsed
    assert "skip" in parsed
    assert isinstance(parsed["run"], list)

