import pandas as pd
import requests
import os
import json

bearer_token = "[insert your own bearer token]"
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def extract_eth(s1):
    s2 = "0x"
	# print("0x{}".format(s1[s1.index(s2) + len(s2):][0:40]))
    try:
        eth = "0x{}".format(s1[s1.index(s2) + len(s2):][0:40])
    except:
        eth = ""
    return eth

def extract_url(s1):
    s2 = "http"
	# print("0x{}".format(s1[s1.index(s2) + len(s2):][0:40]))
    try:
        url = "http{}".format(s1[s1.index(s2) + len(s2):][0:100])
        url = url.split(" ")[0]
    except:
        url = ""
    return url


search_url = "https://api.twitter.com/2/tweets/search/recent"
query_params = {'query': 'from:dumbmeta OR from:dumbcryptopunks','tweet.fields': 'author_id','max_results': 100}
tweet_fields = 'author_id,in_reply_to_user_id,conversation_id,created_at,entities,geo,possibly_sensitive,public_metrics,referenced_tweets,source,withheld'

query_params = {'query': 'from:dumbmeta OR from:dumbcryptopunks','tweet.fields': tweet_fields,'max_results': 100}
json_response = connect_to_endpoint(search_url, query_params)

from_df = pd.DataFrame(json_response['data'])
print(len(json_response['data']))

query_params = {'query': 'to:dumbmeta OR to:dumbcryptopunks','tweet.fields': tweet_fields,'max_results': 100}
json_response = connect_to_endpoint(search_url, query_params)
to_df = pd.DataFrame(json_response['data'])
print(len(json_response['data']))


to_df['eth'] = to_df.apply(lambda x: extract_eth(x['text']), axis=1)
from_df['url'] = from_df.apply(lambda x: extract_url(x['text']), axis=1)

to_col = ['text', 'eth', 'author_id', 'id', 'conversation_id','in_reply_to_user_id']
from_col = ['text', 'url', 'author_id', 'id', 'conversation_id','in_reply_to_user_id']

to_col = ['text',
        'eth',
        'author_id',
        'id',
        'conversation_id',
        'in_reply_to_user_id',
        'referenced_tweets',
        'created_at',
        'entities',
        'source',
        'public_metrics',
        'possibly_sensitive',
         ]

from_col = ['text',
            'url',
            'author_id',
            'id',
            'conversation_id',
            'in_reply_to_user_id',
            'referenced_tweets',
            'created_at',
            'entities',
            'source',
            'public_metrics',
            'possibly_sensitive',
            ]

to_df1 = to_df[to_col]
from_df1 = from_df[from_col]


to_df1["id"] = pd.to_numeric(to_df1["id"])
from_df1["id"] = pd.to_numeric(from_df1["id"])


from_df1 = from_df1.reset_index(drop=True)
to_df1 = to_df1.reset_index(drop=True)
from_df1[from_df1['url']!=""].to_csv("from_df2.csv")
to_df1[to_df1['eth']!=""].to_csv("to_df2.csv")