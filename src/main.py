import json

from src import bayes_classifier, config, generator


def run_classification(
    malicious_path: str, output_path: str, n_innocent: int, verbose: bool = False
):
    with open(malicious_path) as f:
        malicious_sessions = json.load(f)

    innocent_sessions = generator.generate_innocent_sessions(
        n=n_innocent, topics=config.INNOCENT_TOPICS
    )
    sessions = malicious_sessions + innocent_sessions
    classified = [
        bayes_classifier.classify_session(
            s, threshold=config.BELIEF_THRESHOLD, verbose=verbose
        )
        for s in sessions
    ]

    with open(output_path, "w") as f:
        json.dump(classified, f, indent=2)
