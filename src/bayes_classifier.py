from typing import List, Tuple

from src.config import BELIEF_THRESHOLD, HIGH_RISK_THRESHOLD
from src.likelihood import estimate_injection_likelihood


def update_belief(prior: float, likelihood: float) -> float:
    numerator = prior * likelihood
    denominator = numerator + (1 - prior) * (1 - likelihood)
    return numerator / (denominator + 1e-6)


def classify_session(
    session: List[str],
    threshold: float = BELIEF_THRESHOLD,
    verbose: bool = False,
) -> List[Tuple[str, float, str]]:
    belief = 0.5
    max_likelihood = 0.0
    results = []

    for prompt in session:
        likelihood = estimate_injection_likelihood(prompt)
        belief = update_belief(belief, likelihood)
        max_likelihood = max(max_likelihood, likelihood)
        label = "malicious" if belief > threshold else "innocent"
        results.append((prompt, belief, label))
        if verbose:
            print(f"{prompt} -> Belief: {belief:.2f}, Label: {label}")

    if max_likelihood > HIGH_RISK_THRESHOLD:
        for i in range(len(results)):
            prompt, belief, _ = results[i]
            results[i] = (prompt, belief, "malicious")
        if verbose:
            print("⚠️ High-risk prompt detected! Forcing session label to 'malicious'.")

    return results
