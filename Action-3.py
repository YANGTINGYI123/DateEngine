# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:01:45 2020

@author: YangTingyi
"""

#导入工具包
import pandas as pd

#数据加载
result=pd.read_csv('car_complain.csv')

print(result)

#数据预处理
result=result.drop('problem',1).join(result.problem.str.get_dummies(','))#投诉标签拆分


#品牌投诉总量
df=result.groupby('brand')['type'].agg('count')
print(df)

#品牌各车型投诉总数
df1=result.groupby(['brand','car_model'])['type'].agg('count')
print(df1)

#哪个品牌的平均车型投诉最多

#求解每个品牌下各个车型投诉总数
df3= result.groupby(['brand','car_model'])['id'].agg(['count'])
print(df3)

#按品牌分别计算其平均值
df4=df3.groupby(['brand']).mean()
print(df4)

#最后用sort_values从大到小排序
df5=df4.sort_values('count',ascending=False)
print(df5)