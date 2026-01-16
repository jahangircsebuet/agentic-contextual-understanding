class MockLLM:
    """
    Fully CrewAI-compatible mock LLM.

    Handles both attribute-style and callable-style
    capability checks used across CrewAI versions.
    """

    def __init__(self, response: str):
        self.response = response

    
    # -------- Capability hooks (callable) --------
    def supports_stop_words(self) -> bool:
        return False

    def supports_json_schema(self) -> bool:
        return False

    def supports_function_calling(self) -> bool:
        return False
    
    def call(
        self,
        messages,
        callbacks=None,
        from_task=None,
        from_agent=None,
        response_model=None,
        **kwargs,
    ):
        # CrewAI expects a string response
        return self.response

    # Optional: for safety if other paths are used
    def invoke(self, *args, **kwargs):
        return self.response

    def __call__(self, *args, **kwargs):
        return self.response

