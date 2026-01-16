import json
from crewai import Crew
from tasks import who_task

def test_who_agent_persona(mock_agents, sample_user_context):
    agent = mock_agents["who"]
    task = who_task(agent, sample_user_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert parsed["component"] == "WHO"
    assert "student" in parsed["summary"].lower()


def test_who_agent_no_sensitive_attributes(mock_agents, sample_user_context):
    agent = mock_agents["who"]
    task = who_task(agent, sample_user_context)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    text = crew.kickoff().raw.lower()

    forbidden = ["religion", "race", "ethnicity", "sexual", "health"]
    for term in forbidden:
        assert term not in text
