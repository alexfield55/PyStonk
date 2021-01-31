from ISStreamer.Streamer import Streamer
import time
import requests

#diamondhands = str(u"💎")

data_type="comment"  
querylist = ["monday", "monday&buy", "monday&hold", "monday&sell",
             "yolo", "GME", "AMC", "this is the way", "like the stock",
             "not selling", "melvin", "to the moon" ]        
after="1611878400"       
subreddit="wallstreetbets"
metadata=[]

marketopens = 1612161000

#this is for that bootleg front end I am using, if we build our own we can get rid of this
ACCESS_KEY = "ACCESS_KEY"
BUCKET_KEY = "BUCKET_KEY"
BUCKET_NAME = "Wall Street Bets Comment Counter"

#function that pulls the data
def get_pushshift_data(data_type, **kwargs):
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

# create a Streamer instance, used for the front end
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

now = time.time()

#while loop to stop at market open in epoch utc
while now < marketopens:
    for i, item in enumerate(querylist):
        #something going on with the next two lines, was working fine last night now is crapping
        #wrapped it in a try/except but still doesnt really help...
        try:
            metadata.append(get_pushshift_data(data_type=data_type, q=item, after=after, subreddit=subreddit, metadata=True).get("metadata"))
            streamer.log(f'{item}', metadata[i].get("total_results"))
        except:
            pass
        
    metadata.clear()
    now = time.time()
streamer.flush()
