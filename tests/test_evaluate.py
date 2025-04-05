from src.evaluate import evaluate_predictions


def test_evaluate_predictions_basic():
    predictions = [[("prompt", 0.9, "malicious")], [("prompt", 0.1, "innocent")]]
    labels = [True, False]
    metrics = evaluate_predictions(predictions, labels)
    assert 0.9 <= metrics["precision"] <= 1.0
    assert 0.9 <= metrics["recall"] <= 1.0


def test_all_outcomes():
    # 1 TP, 1 FP, 1 FN, 1 TN
    predictions = [
        [("prompt", 0.9, "malicious")],  # TP
        [("prompt", 0.9, "malicious")],  # FP
        [("prompt", 0.1, "innocent")],  # FN
        [("prompt", 0.1, "innocent")],  # TN
    ]
    labels = [True, False, True, False]
    metrics = evaluate_predictions(predictions, labels)
    assert all(0 <= v <= 1 for v in metrics.values())
