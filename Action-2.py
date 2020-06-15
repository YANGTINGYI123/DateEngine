# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:53:39 2020

@author: YangTingyi
"""


from pandas import Series,DataFrame
#统计全班成绩
#搭建原始数据表
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df1=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'])
columns=['语文','数学','英语']
#全班成绩统计数据
data=[df1.mean(),df1.min(),df1.max(),df1.var(),df1.std()]
df2=DataFrame(data,index=['mean','min','max','var','std'])
#计算每位学生的总分
df1['总计']=df1.sum(axis=1)
#输出结果
print(df1.sort_values(by='总计',ascending=False))
print(df2)
