from api_client import get_single_post, get_user_posts

posts = get_user_posts(1)

print(posts)
print(type(posts))
