# -*- coding: utf-8 -*-

import sys
import tweepy
import json

ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxx '
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if '#BharathBandh' in status.text.lower():
            with open('delhipol.json', 'w') as outfile:
                json.dump(status, outfile)
                return True

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True 

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True 

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())    
sapi.filter(locations='28.38,76.5,28.64,77.2')
