from api_client import get_posts

post = get_posts(100)

print(post)
print(type(post))
print(post["title"])
