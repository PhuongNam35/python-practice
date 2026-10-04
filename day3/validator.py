REQUIRED_FIELDS = (
    "customer_id",
    "message",
    "channel"
)


def validate_required_fields(data: dict) -> None:
    for field in REQUIRED_FIELDS:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")


def validate_message(message: str) -> None:
    if not isinstance(message, str):
        raise ValueError("Message must be a string")
    if not message.strip():
        raise ValueError("Message cannot be empty")
    if len(message) > 5000:
        raise ValueError("Message exceeds maximum length of 5000 characters")
