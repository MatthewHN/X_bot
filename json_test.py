import praw
import json
import api_keys

# Initialize PRAW with your credentials
reddit = praw.Reddit(client_id=api_keys.reddit_client_id,
                     client_secret=api_keys.reddit_client_secret,
                     user_agent=api_keys.reddit_user_agent
                     )


# Function to fetch and print media metadata of posts from a subreddit
def print_media_metadata_from_subreddit(subreddit_name, limit=3):
    # Access the subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Iterate over the first 'limit' posts in the subreddit
    for submission in subreddit.hot(limit=limit):
        print(f"Title: {submission.title}\nURL: {submission.url}")

        # Check if the submission has media content
        media_metadata = submission.media_metadata if hasattr(submission, 'media_metadata') else None

        # Print the media metadata in JSON format
        if media_metadata:
            print(json.dumps(media_metadata, indent=4))
        else:
            print("No media metadata found for this submission.")
        print("\n----------------------\n")


# Replace 'subreddit_name' with the name of your desired subreddit
print_media_metadata_from_subreddit('aww')
