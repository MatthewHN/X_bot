import praw
import api_keys


def fetch(subreddit_name):
    # Authenticate with praw
    reddit = praw.Reddit(client_id=api_keys.reddit_client_id,
                         client_secret=api_keys.reddit_client_secret,
                         user_agent=api_keys.reddit_user_agent)

    # Get posts from the subreddit
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.hot(limit=3)

    # Extract relevant data and media URLs from posts
    post_data = []
    for submission in posts:
        title = submission.title
        media_url = submission.url
        if 'comments' in media_url:
            print('Es un comentario fijado')
        elif 'gallery' in media_url:
            print('Es un conjunto de imágenes')
        else:
            post_data.append({
                "title": title,
                "media_url": media_url
            })

    return post_data
