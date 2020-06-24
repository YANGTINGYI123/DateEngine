# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:42:30 2020

@author: YangTingyi
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
# 请求URL
#url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-01.shtml'
def get_page_content(request_url):    
# 得到页面的内容
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
# 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

#分析当前页面投诉
def analysis(soup):
    # 找到完整的投诉信息框
    temp=soup.find('div',class_="tslb_b")
#创建dataframe
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list=temp.find_all('tr')
    #tr和td是HTML的标签
    #tr代表行 td代表列

    for tr in tr_list:
    #提取汽车的投诉信息
        temp={}
        td_list=tr.find_all('td')
     #第一个tr没有td 其余都有8个td
        if len(td_list)>0:
         #解析各字段内容
            id,brand,car_model,type,desc,problem,datetime,status=td_list[0].text,td_list[1].text,td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
          #放到dataframe中
            temp['id'],  temp['brand'],  temp['car_model'],  temp['type'],  temp['desc'],  temp['problem'],  temp['datetime'],  temp['status']=id,brand,car_model,type,desc,problem,datetime,status
            df= df.append(temp,ignore_index=True)
    return df
#df=analysis(soup)
#print(df)
page_num=20
base_url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'

#创建dataFrame
result=pd.DataFrame(columns= ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])

for i in range(page_num):
    request_url=base_url+str(i+1)+'.shtml'
    soup=get_page_content(request_url)
    df=analysis(soup)
    #print(df)
    result=result.append(df)
    

result.to_csv('123',index=False)