import string

HIGH_PRIORITY_KEYWORDS = (
    "urgent",
    "immediately",
    "tomorrow",
    "refund",
    "note"
)


def validate_message(message) -> bool:
    return isinstance(message, str) and bool(message.strip())


def find_matched_keywords(message: str) -> list[str]:
    matched_keywords = []
    print(validate_message(message))
    if not validate_message(message):
        raise TypeError("Invalid message")
        # return ["Invalid message"]

    clean_words = [
        word.strip(string.punctuation)
        for word in message.lower().split()
    ]

    for keyword in HIGH_PRIORITY_KEYWORDS:
        if keyword in clean_words:
            matched_keywords.append(keyword)

    return matched_keywords


print(find_matched_keywords(""))
