import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_single_post(post_id: int) -> dict:
    url = f"{BASE_URL}posts/{post_id}"

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    return data


def get_user_posts(user_id: int) -> list[dict]:
    url = f"{BASE_URL}users/{user_id}/posts"

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    data = response.json()

    return data


def create_post(user_id: int, title: str, body: str) -> dict:
    url = f"{BASE_URL}posts"

    payload = {
        "userId": user_id,
        "title": title,
        "body": body
    }

    response = requests.post(url, json=payload, timeout=5)

    response.raise_for_status()

    data = response.json()

    return data
