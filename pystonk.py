# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 08:58:06 2021

@author: jimb
"""

import requests
import pandas as pd
import plotly.express as px
import json

data_type="comment"     # give me comments, use "submission" to publish something
query="monday"          # Add your query
duration="3d"          # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
subreddit="wallstreetbets"
aggs="created_utc"        #"author", "link_id", "created_utc", "subreddit"

def get_pushshift_data(data_type, **kwargs):
    """
    Gets data from the pushshift api.
 
    data_type can be 'comment' or 'submission'
    The rest of the args are interpreted as payload.
 
    Read more: https://github.com/pushshift/api
    """
 
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

data = get_pushshift_data(data_type=data_type,
                          q=query,
                          after=duration,
                          subreddit=subreddit,
                          aggs=aggs).get("data")

df = pd.DataFrame.from_records(data)[["body"]]
print(df)