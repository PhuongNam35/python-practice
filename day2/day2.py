HIGH_PRIORITY_KEYWORDS = ("urgent", "immediately",
                          "tomorrow", "refund", "note")


def classify_priority(message: str) -> list[str]:
    list_result = []
    for keyword in message.lower().split():
        if keyword in HIGH_PRIORITY_KEYWORDS:
            list_result.append(keyword)

    return list_result


print(classify_priority("This is an urgent request, please take noteat about this"))
