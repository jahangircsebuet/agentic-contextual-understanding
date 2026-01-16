# tests/conftest.py
import pytest
from crewai import Crew
from utils import extract_json

@pytest.fixture
def sample_post():
    return {
        "text": "Feeling frustrated about the quota situation. Students deserve fairness.",
        "image_captions": ["Students holding protest signs"],
        "video_captions": [],
        "timestamp": "2025-12-20",
        "platform": "Facebook",
        "surface": "Group",
        "group_topic": "University Students"
    }

@pytest.fixture
def sample_user_context():
    return {
        "persona": "student",
        "post_history": {"education": 0.6, "politics": 0.4},
        "interaction_history": {"activism": 0.7, "memes": 0.3}
    }

@pytest.fixture
def sample_temporal_context():
    return {
        "timestamp": "2025-12-20",
        "keywords": ["quota", "students"],
        "events": ["Student protests reported in late December"]
    }

@pytest.fixture
def sample_surface_context():
    return {
        "platform": "Facebook",
        "surface": "Group",
        "group_topic": "University Students"
    }

@pytest.fixture
def sample_engagement_context():
    return {
        "reactions": {"like": 120, "angry": 30},
        "comment_emotions": {"supportive": 0.6, "toxic": 0.2}
    }

def run_single_task(agent, task):
    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )
    output = crew.kickoff()
    return output

from crewai import Agent
from mock_llm import MockLLM
from mock_outputs import *


from crewai import LLM
def dummy_llm():
    """
    A safe, no-op LLM object that never touches native providers.
    """
    return LLM(
        model="dummy",
        provider="litellm",   # <- critical
        is_litellm=True       # <- critical
    )

DUMMY_LLM = dummy_llm()

@pytest.fixture
def mock_agents():
    agents = {
        "what": Agent(
            role="WHAT",
            goal="Summarize explicit post content.",
            backstory="Test mock WHAT agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "who": Agent(
            role="WHO",
            goal="Infer user persona from history.",
            backstory="Test mock WHO agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "when": Agent(
            role="WHEN",
            goal="Provide temporal context.",
            backstory="Test mock WHEN agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "where": Agent(
            role="WHERE",
            goal="Analyze platform and audience context.",
            backstory="Test mock WHERE agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "how": Agent(
            role="HOW",
            goal="Summarize engagement and sentiment.",
            backstory="Test mock HOW agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "planner": Agent(
            role="Planner",
            goal="Decide which context modules to run.",
            backstory="Test mock Planner agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "verifier": Agent(
            role="Verifier",
            goal="Audit components for grounding and safety.",
            backstory="Test mock Verifier agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
        "synthesizer": Agent(
            role="Synthesizer",
            goal="Combine contextual components into final interpretation.",
            backstory="Test mock Synthesizer agent.",
            llm=DUMMY_LLM,
            verbose=False,
        ),
    }

        # 🔥 Override LLMs AFTER CrewAI initialization
    agents["what"].llm = MockLLM(WHAT_OUTPUT)
    agents["who"].llm = MockLLM(WHO_OUTPUT)
    agents["when"].llm = MockLLM(WHEN_OUTPUT)
    agents["where"].llm = MockLLM(WHERE_OUTPUT)
    agents["how"].llm = MockLLM(HOW_OUTPUT)
    agents["planner"].llm = MockLLM(PLANNER_OUTPUT)
    agents["verifier"].llm = MockLLM(VERIFIER_OUTPUT)
    agents["synthesizer"].llm = MockLLM(SYNTHESIZER_OUTPUT)

    return agents
