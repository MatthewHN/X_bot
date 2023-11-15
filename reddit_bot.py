import praw
import requests


def fetch(subreddit_name):
    # Authenticate with praw
    reddit = praw.Reddit(client_id='8AMrWjja6Blym5QkFW9JKA',
                         client_secret='5fkKh4aDfCxbrk9uX-0qlrPTZtP6PQ',
                         user_agent='script:Puppy fever X bot:v1.0 (by u/Quirky_Virus1917)')

    # Get posts from the subreddit
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.hot(limit=10)

    # Extract relevant data and media URLs from posts
    post_data = []
    for submission in posts:
        title = submission.title
        media_url = submission.url

        post_data.append({
            "title": title,
            "media_url": media_url
        })

    return post_data
