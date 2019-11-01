# -*- coding: utf-8 -*-

import sys
import tweepy
import json

ACCESS_TOKEN = '1038144593756409857-tKyJEJKlMX9PdVZU6eKOcpktq1DEIE'
ACCESS_SECRET = 'fAm6YH0vBxxW9CRlV9xLoOmft0vJJHumx0m4lfxmEMyA1'
CONSUMER_KEY = 'r2NGVOSPpSwFD6KFoOr7IDUt1 '
CONSUMER_SECRET = 'F0lTKRQU1ksdZMYrTUPq990OrtW8ygmORYiIR177Q6g9RsWklL'

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