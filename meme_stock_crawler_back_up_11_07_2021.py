# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 04:52:10 2021

@author: Bolaji Eniwaye
"""

import praw
import datetime as dt
import psaw
from psaw import PushshiftAPI 
import pandas as pd
import cufflinks as cf
import matplotlib.pylab as plt
import datetime
from datetime import timedelta, date
from datetime import datetime
import numpy as np
from pandas.plotting import scatter_matrix
import yfinance as yf
#https://medium.com/@ozan/interactive-plots-with-plotly-and-cufflinks-on-pandas-dataframes-af6f86f62d94
#https://psaw.readthedocs.io/en/latest/
stock_file="nasdaqlisted.txt";
symbol_loc=0;
nasdaq_stock_file="nasdaqtraded.txt";
symbol_loc=1;

user_agent="Bola_Stock_Script"
username="eni95"
password="Engineer1995"


def parse_stock_txt_file(stock_file,symbol_loc):
    full_stock_list = []
    with open(stock_file) as f:
        contents = f.readlines()
    for line in contents:
        full_stock_list.append(line.split('|')) # full_stock_attribute array
    full_stock_names=[]
    for i in range(len(full_stock_list)):
        full_stock_names.append(full_stock_list[i][symbol_loc])
    return full_stock_names

all_stock_names=parse_stock_txt_file(nasdaq_stock_file,symbol_loc)

    



r = praw.Reddit(client_id='TDI0lzRiSdmK6w', client_secret='4u-XvE0xGuzwT8r1letQ8aqrIqQg-w', user_agent='Bola_Stock_Script')
api = PushshiftAPI(r)


start_epoch=int(dt.datetime(2021, 1, 1).timestamp())
end_epoch=int(dt.datetime(2021, 2, 1).timestamp()   )
hot_posts=list(api.search_submissions(after=start_epoch,
                                      before=end_epoch,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10))
freq_dict={}
freq_array=[]
freq_array_tot=[]
def sort_instance_array(red_posts,sort_num,freq_dict,freq_array_tot):
    new_posts=[];
    
    for post in red_posts:
        new_posts.append(post.title)
    my_found_tickers=[];
    try:freq_array_tot
    except:freq_array_tot=[];
    freq_array=[]
    my_post_titles=[];
    try: freq_dict
    except: freq_dict={}
    it=0
    for name in all_stock_names:
        freq_array.append([name,0])
        try: freq_array_tot[it]
        except: freq_array_tot.append([name,0])
        try: freq_dict[name]
        except: freq_dict[name] = []
    #for i in range(len(all_stock_names)):
        #freq_array.append([all_stock_names[i],0])
        #freq_dict[i]=[all_stock_names[i]
        it+=1
    it=0
    
    for arr in all_stock_names:
        for post in new_posts:   
            my_post_titles.append(post)
            arr_form_1=' {} '.format(arr);
            arr_form_2='${} '.format(arr);
            if (arr_form_2 in post) or (arr_form_1 in post):
                my_found_tickers.append(arr_form_2);
                freq_array[it][1]+=1;
                freq_array_tot[it][1]+=1
        freq_dict[arr].append(freq_array[it][1])
        it+=1;
        freq_array_sorted=sorted(freq_array, key=lambda x: -x[1])
        freq_array_sorted_trunc=freq_array_sorted[0:sort_num];
    return(freq_array_sorted_trunc,freq_dict,freq_array_tot)


date_start_pre=[2020,11,15] # year,month,day,
date_end_pre=[2021,5,15]
date_interval= 2#days
date_current=datetime(date_start_pre[0],date_start_pre[1],date_start_pre[2])
date_start=datetime(date_start_pre[0],date_start_pre[1],date_start_pre[2]) #[2021,3,1]
date_end=datetime(date_end_pre[0],date_end_pre[1],date_end_pre[2]) #[2021,3,1]
time_step=1#days
start_date_vec=[];
my_subreddits="wallstreetbets,stocks,investing,pennystocks,cryptocurrency,povertyfinance";
while date_current<date_end:
    #start_epoch=int(dt.datetime(2021, 1, 1).timestamp())
    #end_epoch=int(dt.datetime(2021, 2, 1).timestamp()   )
    start_epoch=int(date_current.timestamp())
    end_temp=date_current + timedelta(days=time_step)
    end_epoch=int(end_temp.timestamp())
    start_date_vec.append(date_current.strftime("%Y-%m-%d"))
    hot_posts=list(api.search_submissions(after=start_epoch,
                                          before=end_epoch,
                                          subreddit=my_subreddits,
                                          filter=['url','author', 'title', 'subreddit'],
                                          limit=100))

    freq_array_sorted_truncated,freq_dict,freq_array_tot=sort_instance_array(hot_posts,20,freq_dict,freq_array_tot)
    #freq_array_sorted_truncated,freq_dict,freq_array_tot=sort_instance_array(hot_posts,20,freq_dict,freq_array_tot)
    date_current= date_current + timedelta(days=time_step)

freq_array_tot_sorted=sorted(freq_array_tot, key=lambda x: -x[1])
freq_array_tot_sorted_trunc=freq_array_tot_sorted[0:5];
print("freq_array_sorted_trunc",freq_array_sorted_truncated,"freq_array_sorted_trunc")
freq_dict_sort_trunc={}
for pair in freq_array_tot_sorted_trunc:
    freq_dict_sort_trunc[pair[0]]=freq_dict[pair[0]]

myList = freq_dict_sort_trunc.items()
myList = sorted(myList) 
x, y = zip(*myList) 

plot1=plt.plot(x, y)
plt.show()








myList = sorted(myList) 
x_1, y_1 = zip(*myList) 
def rep_fun(x,y):
    x_tot=[]
    for j in range(len(x)):
        x_pre=[]
        for k in range(len(y[j])):    
            #x_pre.append(x[j])     
            x_pre.append(k) 
        x_tot.append(x_pre)
    x_tup=tuple(x_tot)
    return(x_tup)
    
x_tup=rep_fun(x_1,y_1);

#fig, ax = plt.subplots()
#for k in range(len(x)):
#   ax.plot(x_tup[k], y_1[k],label=x_1[k])
#ax.plot(activity, dog, label="dog")
#ax.plot(activity, cat, label="cat")
#ax.legend()

#plt.show()
plt.figure()
for k in range(len(x)):
    plt.plot(x_tup[k], y[k],label=x[k])
plt.legend()
plt.show()


numpy_array = np.array(start_date_vec)
transpose = numpy_array.T
transpose_list = transpose.tolist()
list3 = [list(a) for a in zip(x_tup,transpose_list)]


#date_start_pre=[2021,1,15] # year,month,day,
#date_end_pre=[2021,2,15]

start = str("%d-%d-%d" % (date_start_pre[0],date_start_pre[1],date_start_pre[2])) #"2014-01-01"
end   = str("%d-%d-%d" % (date_end_pre[0],date_end_pre[1],date_end_pre[2])) #'2019-1-01'
gme = yf.download('GME',start,end)
gme['Open'].plot(label = 'TCS', figsize = (15,7))

plt.title('Stock Prices of TCS, Infosys and Wipro')
    #d=str("blah  %d" % 5)
plt.show()
x_values = [datetime.strptime(d,"%Y-%m-%d").date() for d in start_date_vec]
#for k in range(len(x)):
for k in [1,3,4]:
    try:
        p=plt.plot(x_values, y[k],label=x[k]+' post rate')
        a = yf.download(x[k],start,end)
        a['Open']=a['Open']*np.max(y[k])/np.max(a['Open'])
        a['Open'].plot(label = x[k]+' norm price', figsize = (15,7),ls=':',color=p[0].get_color())
    except:
        continue
plt.legend()
plt.gcf().autofmt_xdate()
#gme['Open']=gme['Open']*np.max(y[k])/np.max(gme['Open'])
#gme['Open'].plot(label = 'TCS', figsize = (15,7),ls=':')

plt.title('Reddit post rate vs norm stock')
plt.show()

#freq_array_sorted_truncated.iplot(kind="histogram", bins=20, theme="white", title="Passenger's Ages",xTitle='Ages', yTitle='Count')