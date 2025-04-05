from typing import List


def tokenize_chat_session(session: List[str]) -> List[str]:
    return [token for prompt in session for token in prompt.split()]
