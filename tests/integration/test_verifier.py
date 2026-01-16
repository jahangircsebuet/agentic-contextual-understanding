# tests/test_verifier.py
from agents import verifier_agent
from tasks import verifier_task
from test_conftest import run_single_task
import json

def test_verifier_structure():
    fake_input = {
        "post": {"text": "test"},
        "routing_plan": {"run": ["WHAT"]},
        "components": {
            "WHAT": {
                "summary": "A protest post",
                "key_claims": ["Students protesting"],
                "evidence_used": ["text"],
                "uncertainty": "medium"
            }
        }
    }

    task = verifier_task(verifier_agent, fake_input)
    output = run_single_task(verifier_agent, task)

    data = json.loads(output)
    assert "flags" in data
    assert "revised_components" in data
