import json
import requests

from api_client import get_single_post, get_user_posts, create_post


def main():
    try:
        post = create_post(
            user_id=1,
            title="My New Post abc",
            body="This is the content of my new post."
        )
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")
    else:
        print(json.dumps(post, indent=4))


if __name__ == "__main__":
    main()
