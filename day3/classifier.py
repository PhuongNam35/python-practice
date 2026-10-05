HIGH_PRIORITY_KEYWORDS = (
    "urgent",
    "immediately",
    "tomorrow",
    "refund",
    "note",
)


def normalized_message(message: str) -> str:
    return message.lower().strip()


def find_matched_keywords(message: str) -> list[str]:
    matched_keywords = []
    normalized_message = normalized_message(message)

    for keyword in HIGH_PRIORITY_KEYWORDS:
        if keyword in normalized_message:
            matched_keywords.append(keyword)

    return matched_keywords
