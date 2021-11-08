#pip install praw
#or
#conda install -c conda-forge praw
import praw

print('hey')
reddit = praw.Reddit(client_id='my_client_id', client_secret='my_client_secret', user_agent='my_user_agent')

#print(reddit)
hot_posts = reddit.subreddit('OTCstocks').hot(limit=10)
print(hot_posts)
for post in hot_posts:
    print(post.title)