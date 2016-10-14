# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:44:57 2016

@author: 100635169
"""

import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

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

altcoindata = db.altcoin.find()
bitcoindata = db.bitcoin.find()
coindeskdata = db.coindesk.find()
cryptocurrencydata = db.cryptocurrency.find()
golddata = db.gold.find()
appldata = db.appl.find()
googdata  =db.goog.find()
yhoodata = db.yhoo.find()
        
tweets = pd.DataFrame()
    
keywords = ['altcoin', 'bitcoin', 'coindesk', 'crypto', 'gold', 'appl', 'goog', 'yhoo']
tweets_keywords = [(altcoindata.count()/7), (bitcoindata.count()/7),(coindeskdata.count()/7),
                   (cryptocurrencydata.count()/7),(golddata.count()/7),(appldata.count()/7),
(googdata.count()/7),(yhoodata.count()/7)]                   
x_pos = list(range(len(keywords)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_keywords, width, alpha=1, color='g')

#setitng axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize = 15)
ax.set_title('Daily number of tweets with keywords', fontsize = 10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(keywords)
plt.grid()


altuser = []
for document in altcoindata:
    if document['user']['id'] not in altuser:
        altuser.append(document['user']['id'])

bituser = []
for document in bitcoindata:
    if document['user']['id'] not in bituser:
        bituser.append(document['user']['id'])

coinuser = []
for document in coindeskdata:
    if document['user']['id'] not in coinuser:
        coinuser.append(document['user']['id'])

cryptouser = []
for document in cryptocurrencydata:
    if document['user']['id'] not in cryptouser:
        cryptouser.append(document['user']['id'])

golduser = []
for document in golddata:
    if document['user']['id'] not in golduser:
        golduser.append(document['user']['id'])

appluser = []
for document in appldata:
    if document['user']['id'] not in appluser:
        appluser.append(document['user']['id'])

googuser = []
for document in googdata:
    if document['user']['id'] not in googuser:
        googuser.append(document['user']['id'])

yhoouser = []
for document in yhoodata:
    if document['user']['id'] not in yhoouser:
        yhoouser.append(document['user']['id'])

tweets_keywords = [(len(altuser)/7),(len(bituser)/7),(len(coinuser)/7),(len(cryptouser)/7), (len(golduser)/7),
                   (len(appluser)/7), (len(googuser)/7), (len(yhoouser)/7)]
x_pos = list(range(len(keywords)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_keywords, width, alpha=1, color='g')

#setitng axis labels and ticks
ax.set_ylabel('Number of users', fontsize = 15)
ax.set_title('Daily number of unique user', fontsize = 10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(keywords)
plt.grid()
        