import requests

data_type="comment"  
q = "monday"        
after="1611878400"
subreddit="wallstreetbets"

def get_pushshift_data(data_type, **kwargs): 
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

metadata = get_pushshift_data(data_type=data_type, q=q, after=after, 
                              subreddit=subreddit, metadata=True).get("metadata")
print(metadata.get("total_results"))
