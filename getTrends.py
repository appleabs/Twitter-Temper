import time

startTime = time.time()
try:
    import json
except ImportError:
    import simplejson as json

import requests

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from functools import reduce

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '20840202-dlKS5jTAWgNtgFz4PStRKhvRTlU02Dr9fs17fqYpo'
ACCESS_SECRET = 'RkOaCUh4woM8afDkFMNoGD7T9ZLdyTiJI4i6o7Wg9T8bB'
CONSUMER_KEY = 'Dvk6tiPbXsICMtvEm1VzydrwO'
CONSUMER_SECRET = 'ti8X8RlOSsmakRnoVyNBCgEgqg0qtPE8fKzF2jrLAmh8X0LoM0'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter API
twitter = Twitter(auth=oauth)

trendSearch = twitter.trends.place(_id = 23424977 ) #US
#trendSearch = twitter.trends.place(_id = 23424900 ) #Mexico
#trendSearch = twitter.trends.place(_id = 23424975 ) #UK

trendData = trendSearch[0]['trends']
tweetData = []

print("Trends")
for x in range(0,1):
    print("\n " + trendData[x]['name'])
    tweetSearches = twitter.search.tweets(q=trendData[x]['name'],count=10)['statuses']
    for i in range(0,len(tweetSearches)):
        tweetData.append(tweetSearches[i]['text'])

w, h = 2, len(tweetData);
Matrix = [{0 for x in range(w)} for y in range(h)]

for x in range(0,len(tweetData)):
    Matrix[x] = {"text":tweetData[x],"language":"auto"}

#print(Matrix)

trendsJson2 = {"data":Matrix}
testData = "{'data': [{'text': 'I love Titanic.'}]}"
trendsJson3 = json.dumps(trendsJson2)

r = requests.post("http://www.sentiment140.com/api/bulkClassifyJson?charliepostgate@hotmail.co.uk",data=trendsJson3)

response = json.loads(r.text)
response = response['data']

polarityList = []

for x in range(0,len(response)):
    polarityList.append(response[x]['polarity'])

total = 0
for x in range(0,len(polarityList)):
    total = total + polarityList[x]

print("\nno. of tweets: " + str(len(polarityList)))
print("total: " + str(total))
print("average: " + str(total/len(polarityList)))
print("time taken: " + str(time.time() - startTime))
