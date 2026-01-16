WHAT_OUTPUT = """
{
  "component": "WHAT",
  "summary": "The post discusses student dissatisfaction with quota policies.",
  "key_claims": ["Students are protesting quota decisions"],
  "evidence_used": ["post text", "image captions"],
  "uncertainty": "low"
}
"""

WHO_OUTPUT = """
{
  "component": "WHO",
  "summary": "The user exhibits posting patterns consistent with a student persona.",
  "key_claims": ["Frequent discussion of student issues"],
  "evidence_used": ["post history", "interaction history"],
  "uncertainty": "medium"
}
"""

WHEN_OUTPUT = """
{
  "component": "WHEN",
  "summary": "The post coincides with reported student protests in December 2025.",
  "key_claims": ["Student protests reported around posting time"],
  "evidence_used": ["news search"],
  "uncertainty": "medium"
}
"""

WHERE_OUTPUT = """
{
  "component": "WHERE",
  "summary": "The post was shared in a Facebook group focused on university students.",
  "key_claims": ["Audience is student-focused"],
  "evidence_used": ["group metadata"],
  "uncertainty": "low"
}
"""

HOW_OUTPUT = """
{
  "component": "HOW",
  "summary": "Audience reactions indicate strong emotional engagement and support.",
  "key_claims": ["High anger and support reactions"],
  "evidence_used": ["reaction counts"],
  "uncertainty": "low"
}
"""

PLANNER_OUTPUT = """
{
  "run": ["WHAT", "WHO", "HOW", "WHERE"],
  "skip": ["WHEN"],
  "rationale": {"WHEN": "No explicit temporal references"},
  "confidence": 0.82
}
"""

VERIFIER_OUTPUT = """
{
  "flags": [],
  "component_confidence": {
    "WHAT": 0.9,
    "WHO": 0.7,
    "WHEN": 0.5,
    "WHERE": 0.9,
    "HOW": 0.8
  },
  "revised_components": {},
  "global_notes": "No major issues detected."
}
"""

SYNTHESIZER_OUTPUT = """
{
  "context_object": {
    "WHAT": "Student protest discussion",
    "WHO": "Likely student",
    "WHEN": "Unclear",
    "WHERE": "Facebook student group",
    "HOW": "Strong engagement"
  },
  "final_summary": "The post reflects student frustration with quota policies, shared in a student-focused Facebook group with strong audience engagement.",
  "confidence": {
    "overall": 0.82,
    "per_component": {
      "WHAT": 0.9,
      "WHO": 0.7,
      "WHEN": 0.5,
      "WHERE": 0.9,
      "HOW": 0.8
    }
  },
  "limits": ["Temporal context is uncertain"]
}
"""
