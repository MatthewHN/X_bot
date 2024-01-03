import os
import reddit_bot
import media_downloader
import twitter_bot
import random
import time


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
    posted = False
    while not posted:
        # Specify the subreddit of choice
        subreddits = ['aww', 'puppies', 'TuckedInPuppies', 'PuppySmiles', 'FunnyPuppies', 'rarepuppers', 'Eyebleach', 'dogpictures', 'goldenretrievers', 'germansheperds', 'Dachshund']
        subreddit_name = random.choice(subreddits)
        #subreddit_name = 'TuckedInPuppies'#In case I want to try with a specific subreddit
        print(subreddit_name)
        # Fetch media from Reddit
        posts = reddit_bot.fetch(subreddit_name)

        # Process and post each media item
        for post in posts:
            if posted == False:
                title = post["title"]
                media_url = post["media_url"]

                if media_url:
                    # Download the media
                    filename = f"{title}.jpg" if media_url.endswith(".jpg") or media_url.endswith(".png") or media_url.endswith(
                        ".jpeg") else f"{title}.mp4"
                    file_path = os.getcwd() + '/downloaded_files/' + filename
                    if os.path.exists(file_path):
                        print("Repeated post, not posting")
                        continue
                    if media_downloader.download_media(media_url, filename, 'downloaded_files'):
                        # Post the media to Twitter
                        if twitter_bot.post_tweet(f"{title}", file_path):
                            posted = True
                    else:
                        print(f"Failed to download media for '{title}'.")
                else:
                    print("No media URL")
            else:
                break

    time.sleep(60 * 60 * 4)
    main()


if __name__ == "__main__":
    main()
