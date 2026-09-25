HIGH_PRIORITY_KEYWORDS = ("urgent", "immediately", "tomorrow", "refund")


def classify_priority(message):
    if not isinstance(message, str):
        return "Invalid messagge"
    if any(keyword in message.lower() for keyword in HIGH_PRIORITY_KEYWORDS):
        return "High Priority"
    return "Normal Priority"


print(classify_priority("This is an URGEntality request"))
