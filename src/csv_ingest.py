import ast
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
            prompt = row["prompt"].strip()
            choices_raw = row.get("choices", "").strip()

            sessions[session_id].append(f"User: {prompt}")

            content = ""
            if choices_raw:
                try:
                    parsed = ast.literal_eval(choices_raw)
                    content = parsed[0].get("message", {}).get("content", "").strip()
                except Exception:
                    content = ""

            if content:
                sessions[session_id].append(f"Assistant: {content}")

    data = list(sessions.values())
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Convert chat CSV to JSON sessions")
#     parser.add_argument("csv_path", help="Path to input CSV file")
#     parser.add_argument("json_out", help="Path to output JSON file")

#     args = parser.parse_args()
#     convert_csv_to_sessions(args.csv_path, args.json_out)
