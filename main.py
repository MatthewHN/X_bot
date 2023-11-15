import os
import tweepy
from reddit_bot import initialize_reddit, fetch_media_posts
from twitter_bot import post_to_twitter
from media_downloader import download_media

# Reddit and Twitter credentials
reddit_client_id = '8AMrWjja6Blym5QkFW9JKA'
reddit_client_secret = '5fkKh4aDfCxbrk9uX-0qlrPTZtP6PQ'
reddit_user_agent = 'script:Puppy fever X bot:v1.0 (by u/Quirky_Virus1917)'

twitter_consumer_key = 'apMQ6gPAJV7dMpQrsLQlTFh6L'
twitter_consumer_secret = 'kHEDiFaVzALch8XkBqyqkZ2eereq9v3Vd4WFdhSIYdT7FjF8nI'
twitter_access_token = '1724193786748710912-2TqJhNI0U2lNhO8XC8kvyZIIpG2OCo'
twitter_access_token_secret = 'B3FBYHsDps7SDPhDxLOWip8vi3Hvd8KNEbshGzgqqY5vc'

auth = tweepy.OAuth1UserHandler(
    consumer_key='apMQ6gPAJV7dMpQrsLQlTFh6L',
    consumer_secret='kHEDiFaVzALch8XkBqyqkZ2eereq9v3Vd4WFdhSIYdT7FjF8nI',
    access_token='1724193786748710912-2TqJhNI0U2lNhO8XC8kvyZIIpG2OCo',
    access_token_secret='B3FBYHsDps7SDPhDxLOWip8vi3Hvd8KNEbshGzgqqY5vc'
)

#
def main():
    reddit = initialize_reddit(reddit_client_id, reddit_client_secret, reddit_user_agent)
    twitter_api = tweepy.API(auth, wait_on_rate_limit=True)

    posts = fetch_media_posts(reddit, 'puppies')
    for title, url in posts:
        filename = download_media(url, 'temp_media_file')
        if filename:
            post_to_twitter(twitter_api, filename, title)
            #os.remove(filename)


if __name__ == "__main__":
    main()