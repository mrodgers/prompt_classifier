def estimate_injection_likelihood(prompt: str, context: str = "") -> float:
    return 0.9 if "ignore" in prompt.lower() or "shell" in prompt.lower() else 0.1


def query_llm_likelihood(prompt: str, intent_type: str, model: str = "gpt-4") -> float:
    return 0.8 if intent_type == "malicious" else 0.2
