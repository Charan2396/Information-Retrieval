
import tweepy
import json
import os
import jsonpickle

consumer_key= "XAowutdob8IOggCjcSdBB47Gf"
consumer_secret="dcevFj3NyIL245p7V2qwuCBMi97BN70gGXakpvr37aQbQSDdo7"
access_token="1038144593756409857-Thes02wIWfwY0kAbNgbJk1qcP3BxAb"
access_token_secret="ps8B0AmQVHhK1ndqvYLKRRJsmqBtn0e5bXOaradUzb2i3"

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