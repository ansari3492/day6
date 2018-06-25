# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:12:43 2018

@author: Lenovo
"""


# importing the module
import tweepy
 
# personal details
consumer_key ="ls8K8l6TdkRINWd7HNOK4MRZT"
consumer_secret ="J6E6xs5uFqg0c7uY6qabBpCQjiXA79whnFjNpAPTQRFMs7JuAB"
access_token ="776659819113558016-i3hl6nK992gB6fZT8uvgXbE7tM38GZa"
access_token_secret ="b53JQhB2eGVrplh7WY95epkhALRWR9z0psZCkAJgCy9fT"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status

api.update_status(status ="Hello")