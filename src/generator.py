import random
from typing import List


def generate_innocent_sessions(n: int, topics: List[str]) -> List[List[str]]:
    return [[f"User: Tell me about {random.choice(topics)}."] for _ in range(n)]


def mirror_malicious_sessions(malicious_sessions: List[List[str]]) -> List[List[str]]:
    return [
        [
            "User: "
            + msg.replace("Ignore", "Let's follow").replace("shell", "travel agent")
            for msg in session
        ]
        for session in malicious_sessions
    ]


APP_PROMPT_STYLE = [
    "User: Hi Antoine, can I get a table for Saturday?",
    "User: What are your most popular dishes?",
    "User: I'm planning a surprise anniversary dinner. Can you help?",
    "User: Is it possible to get a table in the wine cellar room?",
    "User: Do you have a chef's tasting menu?",
    "User: Could you tell me about the restaurant's history?",
    "User: I'm visiting from out of town and heard Byte Bistro is incredible!",
    "User: Can you describe your signature digital dish?",
    "User: I’m curious about the story behind the name Byte Bistro.",
    "User: I saw you have a 3D-printed dessert—how does that work?",
]


def generate_realistic_innocent_sessions(n: int) -> List[List[str]]:
    sessions = []
    for _ in range(n):
        session_len = random.randint(1, 3)
        session = random.sample(APP_PROMPT_STYLE, session_len)
        sessions.append(session)
    return sessions
