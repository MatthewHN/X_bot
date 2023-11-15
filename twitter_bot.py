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

# Create API object
#API = tweepy.API(auth, wait_on_rate_limit=True)


def post_to_twitter(twitter_api, filename, status_text):
    try:
        if filename:
            # Post a tweet with an image
            media = twitter_api.media_upload(filename)
            client.create_tweet(text=status_text, media_ids=[media.media_id])
        else:
            # Post a text-only tweet
            client.create_tweet(text=status_text)
    except Exception as e:
        print(f"An error occurred while posting to Twitter: {e}")
