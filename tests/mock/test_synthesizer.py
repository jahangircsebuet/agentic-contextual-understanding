import json
from crewai import Crew
from tasks import synthesis_task

def test_synthesizer_generates_final_summary(mock_agents):
    agent = mock_agents["synthesizer"]

    fake_context = {
        "verified_components": {
            "WHAT": {"summary": "Student protest"},
            "WHO": {"summary": "Likely student"}
        },
        "component_confidence": {
            "WHAT": 0.9,
            "WHO": 0.7
        },
        "verifier_notes": "Temporal context unclear"
    }

    task = synthesis_task(agent, fake_context)
    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "final_summary" in parsed
    assert "confidence" in parsed
    assert "limits" in parsed
