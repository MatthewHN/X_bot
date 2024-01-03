import praw
import api_keys

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id=api_keys.reddit_client_id,
                     client_secret=api_keys.reddit_client_secret,
                     user_agent=api_keys.reddit_user_agent
                     )


# Function to fetch and print media URLs of posts from a subreddit
def print_media_urls_from_subreddit(subreddit_name, limit=3):
    # Access the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Iterate over the first 'limit' posts in the subreddit
    for submission in subreddit.hot(limit=limit):
        print(f"Title: {submission.title}\nURL: {submission.url}")


print_media_urls_from_subreddit('aww')
