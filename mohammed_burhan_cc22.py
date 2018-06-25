# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:52:14 2018

@author: Lenovo
"""

import oauth2
import urllib.request
import time
import json
url1 = "https://api.twitter.com/1.1/search/tweets.json"
params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }
 
consumer = oauth2.Consumer(key="hJhB4Zzct8W1rGJA4uEAY1Kkz", 
                           secret="sx6uMYqqJp2tSQCL0Zv1Yj9J6WisLRKc8dcromeLW7qrm0RXoN")

token = oauth2.Token(key="997358231293841408-853xtoJ85pf7kxE3nq68wRqu0UQix1p",
                     secret="loViEzqMfTeXhtzHfJ7xKrrwt59d3GUJLJX7DZSpepnUS")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key
params["q"]='burhan'
req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib.request.Request(url)
data = json.load(urllib.request.urlopen(response))
filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()