# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:54:03 2019

@author: 11319
"""

import requests
import time     
import re      
from bs4 import BeautifulSoup

data = []
numPages = int(input("Enter how many pages you want to see: "))
movie=str(input("Enter movie name: "))
my_headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
for k in range(1,numPages+1):

    page = 'https://rottentomatoes.com/m/'+ movie +'/reviews?type=&sort=&page='+str(k) 
    src  = False
    for i in range(1,6): 
        try:
            response = requests.get(page, headers = my_headers)
            src = response.content
            break 
        except:
            print ('failed attempt #',i)
            time.sleep(2)
    if not src:
       print('Could not get page: ', page)
       continue 
    else:
       print('Successfully got page: ', page)

    soup = BeautifulSoup(src.decode('ascii', 'ignore'), 'lxml')
    inf= soup.find_all('div',class_="row review_table_row")
    for infor in inf:
        inf_name="NA"
        inf_source="NA"
        inf_time="NA"
        inf_content="NA"
        inf_fresh="NA"
        a=infor.find("a")
        if a:            
            inf_name=a.string
        em=infor.find("em")
        if em:
            inf_source= em.string
        time=infor.find('div',class_="review-date subtle small")
        if time:    
            inf_time=time.string.strip()
        content= infor.find('div',class_="the_review")
        if content:
            inf_content=content.string.strip()
        fresh=infor.find('div',class_='col-xs-16 review_container').find('div')
        if fresh:
            inf_rate= fresh['class'][-1]
        data.append([inf_name,inf_rate, inf_source, inf_time, inf_content])

with open("Yucheng_Zhang_fight_club.txt","w",encoding= "utf-8") as f:
    for comment in data:
        f.write(str(comment[0]) + '\t' + str(comment[1]) + '\t' +str(comment[2]) + '\t'+str(comment[3])+  '\t' +  str(comment[4]) + '\n')
