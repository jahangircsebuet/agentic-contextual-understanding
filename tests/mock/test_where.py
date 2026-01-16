import json
from crewai import Crew
from tasks import where_task

def test_where_agent_platform_context(mock_agents, sample_surface_context):
    agent = mock_agents["where"]
    task = where_task(agent, sample_surface_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "environment" in parsed or "audience" in parsed
