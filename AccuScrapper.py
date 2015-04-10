# works with python 3.4!!! because of nasty unicode problem on 2.7 =(, thx to ° sign :)
# please DONT SPAM OPENING WEB PAGE ON ACCUWEATHER (beacuse I like them) !!!! you can just read page once and then develop everything!!!
from bs4 import BeautifulSoup as bs
#import urllib2
import time
import urllib.request
import datetime
#fileAccu = "storage/emulated/0/pogAccu.txt" #additional path for ANdroid device if you want to run QPython
fileAccu = 'weathergAccu.txt' #here everything will be stored

def start(): #this function connects with given web address
    address = 'http://www.accuweather.com/pl/pl/warsaw/274663/current-weather/274663'
    html = urllib.request.urlopen(address) #maybe try to add an exception or loop in case when page will be not opened TODO
    soup = bs(html) #creating soup from opened web page
    return soup

def forecast():
    fore =  start().find('div', {'id' : 'detail-now'}).find('span', {'class' : 'cond'}).text #gathering forecast
    return fore

def temperature():
    tmp = start().find('div', {'id' : 'detail-now'}).find('span', {'class' : 'temp'}).text #taking temperatore
    #tmp = str(table).replace('<span class="temp">', '').replace('<span>°</span></span>','').strip()
    if "↑" in tmp or "↓" in tmp: #getting rid of this arrow character, but you can delete these two lines if you want
        tmp = tmp.replace('↑', '').replace('↓','')
    return tmp

def pressure():
    table = start().find('div', {'class':'more-info'}).find('ul', {'class':'stats'})
    table = table.find_all('li') 
    pr = str(table[1]).replace('<li>Ciśnienie: <strong>','').replace('</strong></li>', '')\
        .replace('/strong></li>','').strip() #becasue pressure is returned in list of 'li' items

    if "↑" in pr or "↓" in pr: # bye bye arrows
        pr = pr.replace('↑', '').replace('↓','')
    return pr

def clouds(): 
    cl = start().find('div', {'class':'more-info'}).find('ul', {'class':'stats'})
    # tableZach= tableZach.find('ul', {'class':'stats'})
    cl = cl.find_all('li') # as you can see it's taken from 'li' list
    cl= str(cl[3]).replace('<li>Zachmurzenie: <strong>','').replace('</strong></li>','').strip()
    # cl = str(tableZach[3]).replace('<li>Zachmurzenie: <strong>', '').replace('</strong></li>', '').strip()
    if "↑" in cl or "↓" in cl:
        cl = cl.replace('↑', '').replace('↓','')
    return cl

def writer(): #main thing writing results to text file!
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M")
    print(now)
    f = open(fileAccu, 'a')
    f.write(now + '\t' + temperature() + '\t' + forecast() + '\t' + clouds() + '\t'+ pressure() +'\n')
    f.close()
    
#write own method to use this functions
#TODO store data in sql database online; interacting with script via email msg;
