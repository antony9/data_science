# -*- coding: utf-8 -*-

# read data
import json

data_set = None
with open('./data_set/nyc_social_media/rows.json') as social_media_file:
    data_set = json.load(social_media_file)

columns = [ item['name'] for item in data_set['meta']['view']['columns']]

'''
[u'sid', u'id', u'position', u'created_at', u'created_meta', 
u'updated_at', u'updated_meta', u'meta', 
u'Agency', u'Platform', u'Url', u'Date Sampled', 
u'Likes/Followers/Visits/Downloads']
'''

data = data_set['data']

from pandas import DataFrame, Series
import pandas as pd

df = DataFrame(data=data, columns=columns)

totals = df[df['Url']=='TOTAL'].axes[0]

df = df.drop(totals)

platform_counts = df['Platform'].value_counts()
platform_counts.plot(kind='barh', rot=0)

