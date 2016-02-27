import requests
import json
import base64
import config
import random
import argparse

# encode_consumer_key_and_secret
# ------------------------------
# Returns encrypted consumer key/secret combination as specified by this documentation:
# https://dev.twitter.com/oauth/application-only
def encode_consumer_key_and_secret(consumer_key="", consumer_secret=""):
    full_key = (consumer_key + ":" + consumer_secret).encode("utf-8")

    return base64.b64encode(full_key).decode("utf-8")

# grab_bearer_token
# -----------------
# Request for application only token key and secret as specified by this documentation:
# https://dev.twitter.com/oauth/application-only
def grab_bearer_token(consumer_key="", consumer_secret=""):
    url = "https://api.twitter.com/oauth2/token"
    encoded_key_secret_combo = encode_consumer_key_and_secret(config.consumer_key, config.consumer_secret)

    headers = {
        'Authorization': "Basic " + encoded_key_secret_combo,
        'Content-Type': "application/x-www-form-urlencoded;charset=UTF-8"
    }

    r = requests.post(url, data="grant_type=client_credentials", headers=headers)

    return r.json()['access_token']

# grab_random_tweet_by_keyword
# ----------------------------
# Grabs a single random tweet based on keyword.
def grab_random_tweet_by_keyword(keyword="", consumer_key="", consumer_secret="", tweets_to_grab=10):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    bearer_token = grab_bearer_token(consumer_key, consumer_secret)

    headers = {
        'Authorization': "Bearer " + bearer_token,
        'Accept-Encoding': "gzip"
    }

    params = {
        'q': keyword,
        'result_type': "recent",
        'count': tweets_to_grab
    }

    r = requests.get(url, headers=headers, params=params)
    tweets = r.json()['statuses']
    random_tweet = tweets[random.randint(0, len(tweets) - 1)]

    return random_tweet

parser = argparse.ArgumentParser()
parser.add_argument("keyword", help="keyword to search for in Twitter", type=str)
keyword = parser.parse_args().keyword

tweet = grab_random_tweet_by_keyword(keyword, config.consumer_key, config.consumer_secret)

print("@" + tweet['user']['screen_name'] + ": " + tweet['text'])
if 'media' in tweet['entities']:
    for media in tweet['entities']['media']:
        print("media: " + media['media_url'])
