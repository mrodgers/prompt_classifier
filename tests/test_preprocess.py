from src.preprocess import tokenize_chat_session


def test_tokenize_chat_session():
    tokens = tokenize_chat_session(["User: Hello there", "User: Weather today?"])
    assert "Hello" in tokens and "Weather" in tokens
