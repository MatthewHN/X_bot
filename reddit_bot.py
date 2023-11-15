import praw


def initialize_reddit(client_id, client_secret, user_agent):
   return praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)


def fetch_media_posts(reddit, subreddit_name, limit=10):
    posts = []
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.hot(limit=limit):
        if post.is_video or 'image' in post.url:
            posts.append((post.title, post.url))
    return posts
