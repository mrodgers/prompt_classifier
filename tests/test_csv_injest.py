import json
import os
import tempfile

from src.csv_ingest import convert_csv_to_sessions


def test_convert_csv_to_sessions():
    csv_content = "sessionId,prompt\nabc,Hello\nabc,How are you?\ndef,Hi there"
    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "in.csv")
        out_path = os.path.join(tmpdir, "out.json")
        with open(in_path, "w") as f:
            f.write(csv_content)
        convert_csv_to_sessions(in_path, out_path)
        with open(out_path) as f:
            sessions = json.load(f)
        assert len(sessions) == 2
        assert any("User:" in msg for session in sessions for msg in session)
