from typing import List, Tuple

from .likelihood import estimate_injection_likelihood


def update_belief(prior: float, likelihood: float) -> float:
    return (prior * likelihood) / (
        (prior * likelihood) + ((1 - prior) * (1 - likelihood))
    )


def classify_session(
    session: List[str], threshold: float, verbose: bool = False
) -> List[Tuple[str, float, str]]:
    belief = 0.5
    results = []
    for prompt in session:
        likelihood = estimate_injection_likelihood(prompt)
        belief = update_belief(belief, likelihood)
        label = "malicious" if belief > threshold else "innocent"
        if verbose:
            print(f"{prompt} -> Belief: {belief:.2f}, Label: {label}")
        results.append((prompt, belief, label))
    return results
