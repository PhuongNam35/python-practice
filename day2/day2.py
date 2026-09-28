HIGH_PRIORITY_KEYWORDS = ("urgent", "immediately",
                          "tomorrow", "refund", "note")


def find_match_keywords(message: str) -> list[str]:
    matched_keywords = []
    message = message.lower()
    for keyword in HIGH_PRIORITY_KEYWORDS:
        if keyword in message:
            matched_keywords.append(keyword)

    return matched_keywords


print(find_match_keywords("This is an urgentality, please take noteat about this"))
