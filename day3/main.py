import json
from validator import validate_required_fields, validate_message
from classifier import classify_message


def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
