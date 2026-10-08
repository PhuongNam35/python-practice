import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"


def get_posts(post_id: int) -> dict:
    url = f"{BASE_URL}posts/{post_id}"

    response = requests.get(url, timeout=5)

    response.status_code
    response.raise_for_status()

    data = response.json()

    return data
