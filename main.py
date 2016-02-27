import oauth2 as oauth
import requests
import time
import json
import base64

# Returns encrypted consumer key/secret combination as specified by this documentation:
# https://dev.twitter.com/oauth/application-only
def encode_consumer_key_and_secret(consumer_key="", consumer_secret=""):
    full_key = (consumer_key + ":" + consumer_secret).encode("utf-8")

    return base64.b64encode(full_key).decode("utf-8")

# Request for application only token key and secret
def request_for_token(consumer_key="", consumer_secret=""):
    # TODO
    return 0

def search_by_keyword(keyword=""):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    token = oauth.Token(key=access_token, secret=access_token_secret)
    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

    params['oauth_token'] = token.key
    params['oauth_consumer_key'] = consumer.key

    client = oauth.Client(consumer, token)

    resp, content = client.request("https://api.twitter.com/1.1/search/tweets.json?q=%40" + keyword)
    tweets = json.loads(content.decode('utf-8'))['statuses']

    for tweet in tweets:
        print(tweet['text'])
        print('-------------')

print(encode_consumer_key_and_secret(consumer_key, consumer_secret))
