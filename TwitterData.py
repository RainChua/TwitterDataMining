# -*- coding: utf-8 -*
"""
Created on Tue Oct  4 11:33:16 2016

@author: 100635169
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json
import time

#user credentials to access Twitter API
consumer_key = 'jhdQKz4OlMRvOQ139FB3pBvg3'
consumer_secret = 'AtE3RhfciTBiMfNgDB3KkYbNAFQawfPXeprKoBKjwdULcwlMf1'
access_token = '223084268-rJtl5BdihfXqLopHdDQn2suWibSfSAMHk6TWS6UL'
access_secret = '894V1djjc8py2y1kkDKFRCRgrJ3G7kcJxkCC6667QhaOZ'
client = MongoClient()
db = client["Tweets"]
altcoin = db['altcoin']
bitcoin = db['bitcoin']
coindesk = db['coindesk']
cryptocurrency = db['cryptocurrency']
gold = db['gold']
appl = db['appl']
goog = db['goog']
yhoo = db['yhoo']
class StdOutListener(StreamListener):
    def on_data(self,data):
        try:
            #print (data)
            tweets = json.loads(data)
            if ('Altcoin' in tweets['text']):
                altcoin.insert_one(tweets)
                return True
            if ('Bitcoin' in tweets['text']):
                bitcoin.insert_one(tweets)
                return True
            if ('Coindesk' in tweets['text']):
                coindesk.insert_one(tweets)
                return True
            if ('Cryptocurrency' in tweets['text']):
                cryptocurrency.insert_one(tweets)
                return True
            if ('Gold' in tweets['text']):
                gold.insert_one(tweets)
                return True
            if ('APPL' in tweets['text']):
                appl.insert_one(tweets)
                return True
            if ('GOOG' in tweets['text']):
                goog.insert_one(tweets)
                return True
            if ('YHOO' in tweets['text']):
                yhoo.insert_one(tweets)
                return True
        except BaseException as e:
            print ("Failed on Data ",str(e))
            time.sleep(5)
            
    def on_error(self,status):
        print(status)

l=StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
stream = Stream(auth,l)
stream.filter(track=['Altcoin','bitcoin','Coindesk','Cryptocurrency','Gold','APPL','GOOG','YHOO'])