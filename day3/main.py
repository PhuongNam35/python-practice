import json
from validator import validate_required_fields, validate_message
from classifier import classify_message

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_json_file(file_path: str, data: dict) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )


def process_message(data: dict) -> dict:
    validate_required_fields(data)

    message = data["message"]

    validate_message(message)

    matched_keywords = find_matched_keywords(message)
    priority = classify_priority(message)

    result = {
        "customer_id": data["customer_id"],
        "message": message,
        "channel": data["channel"],
        "priority": priority,
        "matched_keywords": matched_keywords,
    }

    return result


def main() -> None:
    try:
        data = read_json_file(INPUT_FILE)

        result = process_message(data)

        write_json_file(OUTPUT_FILE, result)

        print("Message processed successfully.")
        print(result)

    except FileNotFoundError:
        print(f"File not found: {INPUT_FILE}")

    except json.JSONDecodeError as error:
        print(f"Invalid JSON: {error}")

    except (TypeError, ValueError) as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
