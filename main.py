import os
import reddit_bot
import media_downloader
import twitter_bot
import time

# Reddit and Twitter credentials
reddit_client_id = '8AMrWjja6Blym5QkFW9JKA'
reddit_client_secret = '5fkKh4aDfCxbrk9uX-0qlrPTZtP6PQ'
reddit_user_agent = 'script:Puppy fever X bot:v1.0 (by u/Quirky_Virus1917)'

twitter_consumer_key = 'apMQ6gPAJV7dMpQrsLQlTFh6L'
twitter_consumer_secret = 'kHEDiFaVzALch8XkBqyqkZ2eereq9v3Vd4WFdhSIYdT7FjF8nI'
twitter_access_token = '1724193786748710912-2TqJhNI0U2lNhO8XC8kvyZIIpG2OCo'
twitter_access_token_secret = 'B3FBYHsDps7SDPhDxLOWip8vi3Hvd8KNEbshGzgqqY5vc'


def get_absolute_file_path(filename):
    # Get the current working directory
    current_directory = os.getcwd()

    # Construct the absolute path
    absolute_path = os.path.join(current_directory, filename)

    # Check if the file exists
    if os.path.exists(absolute_path):
        return absolute_path
    else:
        return "File not found."


def main():
    # Specify the subreddit of choice
    subreddit_name = "puppies"

    # Fetch media from Reddit
    posts = reddit_bot.fetch(subreddit_name)

    # Process and post each media item
    for post in posts:
        title = post["title"]
        media_url = post["media_url"]

        if media_url:
            # Download the media
            filename = f"{title}.jpg" if media_url.endswith(".jpg") or media_url.endswith(".png") or media_url.endswith(
                ".jpeg") else f"{title}.mp4"
            file_path = os.getcwd() + '\\downloaded_files\\' + filename
            if os.path.exists(file_path):
                print("Repeated post, not posting")
                continue
            if media_downloader.download_media(media_url, filename, 'downloaded_files'):
                # Post the media to Twitter
                twitter_bot.post_tweet(f"{title}", file_path)
            else:
                print(f"Failed to download media for '{title}'.")
        else:
            print("No media URL")


if __name__ == "__main__":
    main()
