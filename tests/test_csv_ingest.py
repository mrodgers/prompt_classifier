import json
import os
import tempfile

from src.csv_ingest import convert_csv_to_sessions


def test_convert_csv_to_sessions():
    csv_content = (
        "sessionId,prompt,choices\n"
        "abc,Hello,"
        "\"[{'index': 0, 'message': {'role': 'assistant', "
        "'content': 'Hi there!'}}]\"\n"
        "abc,How are you?,"
        "\"[{'index': 0, 'message': {'role': 'assistant', "
        "'content': 'I am good.'}}]\"\n"
        "def,Hi there,"
        "\"[{'index': 0, 'message': {'role': 'assistant', "
        "'content': 'Hello!'}}]\"\n"
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "in.csv")
        out_path = os.path.join(tmpdir, "out.json")

        with open(in_path, "w") as f:
            f.write(csv_content)

        convert_csv_to_sessions(in_path, out_path)

        with open(out_path) as f:
            sessions = json.load(f)

        assert len(sessions) == 2
        assert all(
            any(role in msg for role in ("User:", "Assistant:"))
            for session in sessions
            for msg in session
        )
        assert any("Hi there!" in msg for session in sessions for msg in session)
        assert any("Hello!" in msg for session in sessions for msg in session)


def test_convert_csv_to_sessions_with_malformed_choices():
    csv_content = (
        "sessionId,prompt,choices\n" 'xyz,Test prompt,"MALFORMED_JSON_NOT_A_LIST"\n'
    )

    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "malformed.csv")
        out_path = os.path.join(tmpdir, "malformed_out.json")

        with open(in_path, "w") as f:
            f.write(csv_content)

        convert_csv_to_sessions(in_path, out_path)

        with open(out_path) as f:
            sessions = json.load(f)

        assert len(sessions) == 1
        assert sessions[0][0].startswith("User:")
        assert all(not msg.startswith("Assistant:") for msg in sessions[0][1:])
