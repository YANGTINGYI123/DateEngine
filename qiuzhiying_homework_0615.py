#!/usr/bin/env python
# coding: utf-8

# In[4]:


#action1
i=2
sum=2
while i<51:
    sum=sum+i*2
    i=i+1
print(sum)


# In[52]:


#action2
#导入工具包
import pandas as pd
from pandas import Series,DataFrame

#创建字典
data={'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}

#将字典转化为DataFrame（数据库）
frame=DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'])
#显示数据库
print(frame)

#计算各科平均成绩
print('--------------各科平均成绩--------------')
print(frame.mean())

#计算各科最小成绩
print('---------------各科最小成绩--------------')
print(frame.min())

#计算各科最大成绩、方差、标准差
print('----------------各科最大成绩、方差、标准差---------------')
print(frame.max())
print(frame.var())
print(frame.std())

#在数据库增加“总成绩”一列，计算方法为该行成绩之和
frame['总成绩']=frame.sum(axis=1)

#将数据按照总成绩排序后显示
print(frame.sort_values('总成绩',ascending=False))


# In[51]:


'''对汽车质量数据进行统计
数据集：car_complain.csv,600条汽车质量投诉
Step1，数据加载
Step2，数据预处理，拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''

#导入工具包
import pandas as pd

#数据加载
result=pd.read_csv('car_complain.csv')

#数据预处理，离散的特征处理

# 将故障类型进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))


print('-----------------------------品牌投诉排行--------------------------------')
#品牌投诉总数
df= result.groupby('brand')['id'].agg(['count'])
#品牌投诉排行
print(df.sort_values('count',ascending=False))


print('--------------------------------品牌各车型投诉排行----------------------------------------')
#品牌各车型投诉总数
df1=result.groupby(['brand','car_model'])['id'].agg(['count'])
#品牌各车型投诉排行榜
print(df1.sort_values('count',ascending=False))


print('--------------------------------品牌平均车型投诉排行----------------------------------------')
#哪个品牌的平均车型投诉最多
df2=df1.groupby('brand').mean()
print(df2.sort_values('count',ascending=False))


# In[ ]:




