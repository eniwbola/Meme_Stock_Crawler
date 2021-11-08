import pandas as pd
import requests
import json
import csv
import time
import datetime

#https://rareloot.medium.com/using-pushshifts-api-to-extract-reddit-submissions-fb517b286563
def getPushshiftData(query, after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?title='+str(query)+'&size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']


def collectSubData(subm):
    subData = list() #list to store data points
    title = subm['title']
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"    
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    permalink = subm['permalink']


sub='OTCstocks'#'PS4'
before = "1635046653" #October 1st
after = "1634269053"  #January 1st 
query = " "
subCount = 0
subStats = {}

data = getPushshiftData(query, after, before, sub)
print(len(data))
it=0
while len(data) > 0:
    for submission in data:
        collectSubData(submission)
        subCount+=1
    # Calls getPushshiftData() with the created date of the last submission
    print(len(data))
    print(str(datetime.datetime.fromtimestamp(data[-1]['created_utc'])))
    after = data[-1]['created_utc']
    data = getPushshiftData(query, after, before, sub)
    it+=1
    print("len(data)",len(data))
    print("it",it)
print(len(data))