import tweepy
from config import *
import time
from random import randint

from read import get_tweet

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

while True:
    minutes = randint(1, 3600)
    INTERVAL = 60 * minutes
    print("Tweeting.")
    tweet = get_tweet()
    api.update_status(tweet)
    print("Tweet Successful")
    time.sleep(INTERVAL)
