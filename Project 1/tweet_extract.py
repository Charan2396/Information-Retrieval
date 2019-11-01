
import tweepy
import json
import os
import jsonpickle

consumer_key= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxf"
consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token="xxxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxx"
access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)

count=0
#ids = set()
with open('tweet2_del_Politics.json','a') as outfile:
    for tweet in tweepy.Cursor(api.search, 
                    q="Politics or राजनीति -filter:retweets", 
                    geocodes="28.644800, 77.216721, 300km",
                                       #since="2018-09-05", 
                    #until="2018-09-18", 
                    lang="hi").items(2000):
        outfile.write(jsonpickle.encode(tweet._json, unpicklable=False)+'\n')
        count+=1
        
       

print("Downloaded tweets", count)
