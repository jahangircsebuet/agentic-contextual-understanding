import json
from crewai import Crew
from tasks import how_task

def test_how_agent_engagement_summary(mock_agents, sample_engagement_context):
    agent = mock_agents["how"]
    task = how_task(agent, sample_engagement_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "sentiment" in parsed
    assert parsed["sentiment"] in ["positive", "negative", "neutral"]

