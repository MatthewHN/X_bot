# In reddit_bot.py or a separate test script

from reddit_bot import initialize_reddit, fetch_media_posts

# Initialize with your actual Reddit credentials
reddit = initialize_reddit('8AMrWjja6Blym5QkFW9JKA', '5fkKh4aDfCxbrk9uX-0qlrPTZtP6PQ', 'script:Puppy fever X bot:v1.0 (by u/Quirky_Virus1917)')

# Fetch posts from a subreddit
posts = fetch_media_posts(reddit, 'puppies', 50)
for title, url in posts:
    print(f"Title: {title}, URL: {url}")
