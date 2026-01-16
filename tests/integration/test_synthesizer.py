# tests/test_synthesizer.py
from agents import synthesizer_agent
from tasks import synthesis_task
from test_conftest import run_single_task
import json

def test_synthesizer_output():
    fake_context = {
        "verified_components": {
            "WHAT": {"summary": "A student protest"},
            "WHO": {"summary": "Likely student activist"}
        },
        "component_confidence": {"WHAT": 0.9, "WHO": 0.7},
        "verifier_notes": "Context is partial"
    }

    task = synthesis_task(synthesizer_agent, fake_context)
    output = run_single_task(synthesizer_agent, task)

    data = json.loads(output)
    assert "final_summary" in data
    assert "confidence" in data
