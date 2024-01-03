import tweepy
import api_keys

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=api_keys.twitter_consumer_key,
    consumer_secret=api_keys.twitter_consumer_secret,
    access_token=api_keys.twitter_access_token,
    access_token_secret=api_keys.twitter_access_token_secret
)

auth = tweepy.OAuth1UserHandler(
    consumer_key=api_keys.twitter_consumer_key,
    consumer_secret=api_keys.twitter_consumer_secret,
    access_token=api_keys.twitter_access_token,
    access_token_secret=api_keys.twitter_access_token_secret
)

api = tweepy.API(auth, wait_on_rate_limit=True)


def upload_media(media_path):
    # Upload the media file to Twitter and return the media ID
    response = api.media_upload(media_path)
    return response.media_id_string


def post_tweet(title, media_path):
    try:
        media_id = upload_media(media_path)
        client.create_tweet(text=title, media_ids=[media_id])
        print(f"Successfully posted '{title}' to Twitter.")
        return True
    except Exception as e:
        print(f"An error occurred while posting to Twitter: {e}")
        return False
