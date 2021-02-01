import json
import requests

querylist = ["monday", "monday&buy", "monday&hold", "monday&sell", "yolo", "GME", "AMC", "this is the way", "like the stock", "not selling", "melvin", "to the moon" ]  

#querylist = ["peloton", "PTON"]

subreddit="wallstreetbets"

#current tacked on sort and size at end for testing
def redditAPIpull(subreddit, commentQuery):
    url = "https://api.pushshift.io/reddit/search/comment/?q="+commentQuery+"&subreddit="+subreddit+"&filter=body"
    r = requests.get(url)
    return r

retList={}
i=0
for i in range(len(querylist)):
        print("\n\n\n***********************************"+querylist[i]+"********************************************************")
        r=redditAPIpull(subreddit,querylist[i])
        response = r.json()
        for i in range(len(response['data'])):
            print((response['data'][i]['body']))
            print(str(i+1)+"***************************************************************************************************************\n\n\n")
