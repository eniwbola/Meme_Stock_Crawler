import praw
import json


#https://stackoverflow.com/questions/5246843/how-to-get-a-complete-list-of-ticker-symbols-from-yahoo-finance

#praw(client_id="vOXOW8rXJhsa5A", client_secret="F7u9eaS0_5dHelXGZiJPqUivtvbWlw", user_agent="stocks_crawler_eni95")
#client_id="TDI0lzRiSdmK6w"
#client_secret="4u-XvE0xGuzwT8r1letQ8aqrIqQg-w"
#my_client_secret=client_secret;


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




print('hey')
reddit = praw.Reddit(client_id='TDI0lzRiSdmK6w', client_secret='4u-XvE0xGuzwT8r1letQ8aqrIqQg-w', user_agent='Bola_Stock_Script')

#print(reddit)
hot_posts = reddit.subreddit('OTCstocks').hot(limit=100)
print('hot_posts',hot_posts)

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
    #hot_posts = reddit.subreddit('OTCstocks').hot(limit=3)
    #for post in hot_posts:   
    for post in new_posts:   
        #print("post",post)
        #print("arr",post.title)
        #print("post_title_type",type(post.title))
        #my_post_titles.append(post.title)
        my_post_titles.append(post)
        arr_form_1=' {} '.format(arr);
        arr_form_2='${} '.format(arr);
        #if (arr_form_2 in post.title) or (arr_form_1 in post.title):
        if (arr_form_2 in post) or (arr_form_1 in post):
            #print("Found!")
            my_found_tickers.append(arr_form_2);
            freq_array[it][1]+=1;
    it+=1;
test_post_title='e ZYXI e';
it=0
for arr in array1D:
    arr_form_1=' {} '.format(arr);
    arr_form_2='${} '.format(arr);
    #print("arr_form_2",arr_form_2);
    #print("arr_form_1",arr_form_1);
    if (arr_form_2 in test_post_title) or (arr_form_1 in test_post_title):
        #print("Found!")
        #print('freq_arr',it)
        freq_array[it][1]+=1;
        #print(it,"Found_end!")
    it+=1
#print("freq_array",freq_array,"freq_array")
freq_array_sorted=sorted(freq_array, key=lambda x: -x[1])
#print("freq_array_sorted",freq_array_sorted,"freq_array_sorted")
freq_array_sorted_trunc=freq_array_sorted[0:20];
print("freq_array_sorted_trunc",freq_array_sorted_trunc,"freq_array_sorted_trunc")
#print("my_found_tickers",my_found_tickers)
#print("my_post_titles",my_post_titles)
#d ="C:\Users\eniwa\OneDrive\Desktop\nasdaqlisted.txt"

#array2D = []

#for filename in os.listdir(d):
#    if not filename.endswith('.txt'):
#        continue

#    with open(filename, 'r') as f:
#        for line in f.readlines():
#            array2D.append(line.split(' '))

#print(array2D)