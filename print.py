import praw
import json

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id='8AMrWjja6Blym5QkFW9JKA',
                     client_secret='5fkKh4aDfCxbrk9uX-0qlrPTZtP6PQ',
                     user_agent='script:Puppy fever X bot:v1.0 (by u/Quirky_Virus1917)')


# Function to fetch and print media URLs of posts from a subreddit
def print_media_urls_from_subreddit(subreddit_name, limit=5):
    # Access the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Iterate over the first 'limit' posts in the subreddit
    for submission in subreddit.hot(limit=limit):
        print(f"Title: {submission.title}\nURL: {submission.url}")


print_media_urls_from_subreddit('puppies')
