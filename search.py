import praw


client = "mcr2Y97j_4r20w" # Client ID
secret = "-kl8BzZcDf3iSJGaJsXQz4rADzc" # Secret key
user_agent = "ios:com.example.myredditapp:v1.2.3 (by /u/kemitche)"

# Function to connect to Reddit API
def connect(cl_id, cl_secret):
    return praw.Reddit(client_id=cl_id, client_secret=cl_secret, user_agent=user_agent)

def search_reddit(query):
    red = connect(client, secret)
   
    # Generating the string for keywords
    keys = query.split(",")
    subs = ["jobbit", "forhire"]

    # Generate string for keys
    str_keys = "(title : \"" +keys[0]+ "\""
    for k in keys[1:]:
        str_keys = str_keys + " OR title:\"" + k + "\""
    str_keys = str_keys + ")"

    # Generate string for subs
    str_subs = "(subreddit:hiring"
    for sub in subs:
        str_subs = str_subs + " OR subreddit:" + sub
    str_subs = str_subs + ") "

    # Creating the full search query using Reddit search syntax
    full_str = "(title:\"hiring\" OR flair:Hiring) AND  " + str_keys + " AND " + str_subs

    # making the call
    all = red.subreddit("all")
    
    return all.search(query=full_str, sort="new")












