from typing import Dict, List, Tuple


def evaluate_predictions(
    predictions: List[List[Tuple[str, float, str]]], ground_truth: List[bool]
) -> Dict[str, float]:
    tp = fp = fn = tn = 0
    for pred, truth in zip(predictions, ground_truth):
        last_label = pred[-1][2] == "malicious"
        if last_label and truth:
            tp += 1
        elif last_label and not truth:
            fp += 1
        elif not last_label and truth:
            fn += 1
        else:
            tn += 1
    precision = tp / (tp + fp + 1e-6)
    recall = tp / (tp + fn + 1e-6)
    f1 = 2 * precision * recall / (precision + recall + 1e-6)
    return {"precision": precision, "recall": recall, "f1": f1}
