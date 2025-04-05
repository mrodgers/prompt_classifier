import csv
import json
from collections import defaultdict
from typing import Dict, List


def convert_csv_to_sessions(csv_path: str, json_out: str) -> None:
    sessions: Dict[str, List[str]] = defaultdict(list)

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            session_id = row["sessionId"]
            prompt = row["prompt"]
            sessions[session_id].append(f"User: {prompt.strip()}")

    data = list(sessions.values())
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
