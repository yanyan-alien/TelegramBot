import tweepy
import re
import datetime
import os
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def main():
    response = client.get_user(username='yanyan_alien')
    user_id = response.data.id
    tweets = client.get_users_tweets(user_id, max_results=5)
    tweet = tweets.data[1]
    cleaned_text = re.sub(r'https://t.co/\w{10}', '',tweet.text)[:-1]
    status = api.get_status(tweet.id, tweet_mode="extended")
    urls = [dic['expanded_url'] for dic in status.entities["urls"]]
    for url in urls:
        if 'vlive' in url or 'youtu.be' in url:
            print(urls)
            return cleaned_text +"\n" + " ".join(urls), status.created_at
    return None, None