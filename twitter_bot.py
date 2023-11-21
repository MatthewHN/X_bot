import tweepy

# Authenticate to Twitter
client = tweepy.Client(
    consumer_key='apMQ6gPAJV7dMpQrsLQlTFh6L',
    consumer_secret='kHEDiFaVzALch8XkBqyqkZ2eereq9v3Vd4WFdhSIYdT7FjF8nI',
    access_token='1724193786748710912-2TqJhNI0U2lNhO8XC8kvyZIIpG2OCo',
    access_token_secret='B3FBYHsDps7SDPhDxLOWip8vi3Hvd8KNEbshGzgqqY5vc'
)

auth = tweepy.OAuth1UserHandler(
    consumer_key='apMQ6gPAJV7dMpQrsLQlTFh6L',
    consumer_secret='kHEDiFaVzALch8XkBqyqkZ2eereq9v3Vd4WFdhSIYdT7FjF8nI',
    access_token='1724193786748710912-2TqJhNI0U2lNhO8XC8kvyZIIpG2OCo',
    access_token_secret='B3FBYHsDps7SDPhDxLOWip8vi3Hvd8KNEbshGzgqqY5vc'
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
