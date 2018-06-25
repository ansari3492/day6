# -*- coding: utf-8 -*-
"""
Created on Sun May 20 22:25:14 2018

@author: Lenovo
"""

import facebook as fb

# Facebook Graphic Explorer API user Access Token
access_token = "EAACEdEose0cBADmZCNOOMZBjr1lTFvhdFlYIxER7yPChC0NCRhBkjIm4tkEHuGnfwkOZA3zdkTetWLsYT0ZBhhll0uz7i3lu5rKgK0g9kIO7HKV53CxOqXICS7EhV3DEfroXxHtvw79zOuVXC4oqjiBn4KvMlYUifzUjWFmoHFIoDBUn7lFKqY3R8HeurV0WVUYMJO45lgZDZD"

# Message to post as status on Facebook
status = "hi everyone this are post through the python APIs"

# Authenticating
graph = fb.GraphAPI(access_token)
post_id = graph.put_photo(image=open("bugatti.jpg","rb"),message="post through REST APIs")

