import oauth2 as oauth
import requests
import time
import json
import base64
import config

# encode_consumer_key_and_secret
# -----------------
# Returns encrypted consumer key/secret combination as specified by this documentation:
# https://dev.twitter.com/oauth/application-only
def encode_consumer_key_and_secret(consumer_key="", consumer_secret=""):
    full_key = (consumer_key + ":" + consumer_secret).encode("utf-8")

    return base64.b64encode(full_key).decode("utf-8")

# request_for_token
# -----------------
# Request for application only token key and secret as specified by this documentation:
# https://dev.twitter.com/oauth/application-only
def request_for_token(consumer_key="", consumer_secret=""):
    url = "https://api.twitter.com/oauth2/token"
    encoded_key_secret_combo = encode_consumer_key_and_secret(config.consumer_key, config.consumer_secret)

    headers = {
        'Authorization': "Basic " + encoded_key_secret_combo,
        'Content-Type': "application/x-www-form-urlencoded;charset=UTF-8"
    }

    r = requests.post(url, data="grant_type=client_credentials", headers=headers)

    return r.json()['access_token']

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

print(request_for_token(config.consumer_key, config.consumer_secret))
