import json
from crewai import Crew
from tasks import verifier_task

# def test_verifier_structure(mock_agents):
#     agent = mock_agents["verifier"]

#     fake_input = {
#         "post": {"text": "Test post"},
#         "routing_plan": {"run": ["WHAT", "WHO"]},
#         "components": {
#             "WHAT": {
#                 "summary": "Student protest post",
#                 "key_claims": ["Students protesting"],
#                 "evidence_used": ["post text"],
#                 "uncertainty": "medium"
#             }
#         }
#     }

#     task = verifier_task(agent, fake_input)
#     crew = Crew(agents=[agent], tasks=[task], verbose=False)
#     output = crew.kickoff()

#     data = json.loads(output)

#     assert "flags" in data
#     assert "component_confidence" in data
#     assert "revised_components" in data
#     assert "global_notes" in data

def test_verifier_structure(mock_agents, sample_context_bundle):
    agent = mock_agents["verifier"]
    task = verifier_task(agent, sample_context_bundle)

    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    parsed = json.loads(crew.kickoff().raw)

    assert "approved" in parsed
    assert "issues" in parsed
    assert isinstance(parsed["issues"], list)

