import tweepy
import textblob

consumer_key = 'Dl3cHW1xGtnnSKV50YexHWMYL'
consumer_sec = 'K2jHO32Pau6MibM9OL7VZc3DmR9ppXPYVp3jPVMSHSpFl6sTxM'
access_token = '1035772077486235648-zheUrHqg6qy5hsiWOyR0Kdaffq6ZfM'
access_token_sec = '3JGmsmBZ5pxLRDvtCHDu2QQGoeZd4M5dH428IMM86CUxv'

auth = tweepy.OAuthHandler(consumer_key,consumer_sec)
auth.set_access_token(access_token,access_token_sec)

api = tweepy.API(auth)

public_tweet = api.search('Trump')

for tweet in public_tweet:
    print(tweet.text)
    analysis = textblob.TextBlob(tweet.text)
    print(analysis.sentiment)
