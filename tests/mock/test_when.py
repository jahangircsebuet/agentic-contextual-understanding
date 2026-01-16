import json
from crewai import Crew
from tasks import when_task

def test_when_agent_temporal_context(mock_agents, sample_temporal_context):
    agent = mock_agents["when"]
    task = when_task(agent, sample_temporal_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "temporal_context" in parsed or "summary" in parsed


def test_when_agent_no_guessing_language(mock_agents, sample_temporal_context):
    agent = mock_agents["when"]
    task = when_task(agent, sample_temporal_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    text = crew.kickoff().raw.lower()

    forbidden = ["might be", "possibly", "could be", "guess"]
    for phrase in forbidden:
        assert phrase not in text
