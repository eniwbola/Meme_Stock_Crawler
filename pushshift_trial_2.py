import praw
import datetime as dt
import psaw
from psaw import PushshiftAPI

#https://medium.com/@ozan/interactive-plots-with-plotly-and-cufflinks-on-pandas-dataframes-af6f86f62d94

#https://psaw.readthedocs.io/en/latest/

array2D = []
it=1;
stock_file="nasdaqlisted.txt";
symbol_loc=0;
stock_file="nasdaqtraded.txt";
symbol_loc=1;
with open(stock_file) as f:
    contents = f.readlines()
   
    if it==1:
        print("yo")
        print(len(contents))
        print(contents[2000])

for line in contents:
    array2D.append(line.split('|'))

print("array2D")
print(array2D[1:][symbol_loc])
print("array2Dlen")
print(len(array2D))
array1D=[]
for i in range(len(array2D)):
    array1D.append(array2D[i][symbol_loc])
print(array1D[1:3])
user_agent="Bola_Stock_Script"

username="eni95"
password="Engineer1995"

r = praw.Reddit(client_id='TDI0lzRiSdmK6w', client_secret='4u-XvE0xGuzwT8r1letQ8aqrIqQg-w', user_agent='Bola_Stock_Script')
api = PushshiftAPI(r)


start_epoch=int(dt.datetime(2021, 1, 1).timestamp())
end_epoch=int(dt.datetime(2021, 2, 1).timestamp()   )
hot_posts=list(api.search_submissions(after=start_epoch,
                                      before=end_epoch,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10))

new_posts=[];
for post in hot_posts:
    print(post.title)
    print("post_title_type",type(post.title))
    new_posts.append(post.title)
my_found_tickers=[];
freq_array=[];
my_post_titles=[];
for i in range(len(array1D)):
    freq_array.append([array1D[i],0])
it=0

for arr in array1D:
    for post in new_posts:   
        my_post_titles.append(post)
        arr_form_1=' {} '.format(arr);
        arr_form_2='${} '.format(arr);
        if (arr_form_2 in post) or (arr_form_1 in post):
            my_found_tickers.append(arr_form_2);
            freq_array[it][1]+=1;
    it+=1;

freq_array_sorted=sorted(freq_array, key=lambda x: -x[1])
freq_array_sorted_trunc=freq_array_sorted[0:20];
print("freq_array_sorted_trunc",freq_array_sorted_trunc,"freq_array_sorted_trunc")
