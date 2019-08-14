#%%
import numpy as np
import pandas as pd
import matplotlib as mql
from matplotlib import pyplot as plt
# 支持中文显示
plt.rcParams['font.family'] = 'kaiti'
# 使用非uncode的符号，当使用中文时候设置
plt.rcParams['axes.unicode_minus'] = False

#%%
# 加载相关数据集
players = pd.read_csv('FullData.csv')
display(players)
players
# 使用head(前)  tail(后)  sample(随机)  大致看下数据集的基本情况
# players.head()
# 设置显示完整的列标签,set_option()，参数：display.[max_categories, max_columns, max_colwidth, max_info_columns,
#  max_info_rows, max_rows, max_seq_items]
# pd.set_option()


#%%
# 数据探索以及清洗
# players.info()
# 对数据整体进行查看，发现National_Position(位置)和National_Kit(号码)存在大量的缺失值
# 但是分析得到，该缺失值为正常现象。

# isnull+any查看缺失值
# players['Club_Position'].isnull().any()
# 找出缺失值的记录 
# players[players['Club_Position'].isnull()]

# 过滤缺失值（布尔数组的运算）
# 使用 notnull过滤，非缺失值返回 True,保留  ，返回缺失值 False,丢弃
players = players[players['Club_Position'].notnull()]
# 再次调用info方法查看缺失值过滤结果
players.info()

#%%
# 异常值处理
# describe方法得到数据的描述性统计信息，比如max,min,mean,std 进行异常值分析
# players.describe()
# 还可以用箱线图辅助查看数据
# 总体
# players.plot(kind='box')
# 指定哪一列，形成箱型图
players[['Rating','Marking']].plot(kind='box')

#%%
# 重复值处理
players.duplicated().any()
# 结果为False,没有重复值

# 如果有重复值，则要根据duplicate得到的布尔数据，将布尔数据传递给players，得到重复值数据
# 参数：keep = 'first/last/False' first:出现重复值，则把第一个为False,后两条为True
#       last : 最后一个为False,前面的都为True  ,False :全部都返回True
# players[players.duplicated()]

# 删除重复著
# drop_duplicates中也是keep参数，理解和duplicated函数的一样，
#  inplace = True  就地删除
players.drop_duplicates(0)

#%%
# 身高和体重处理
# players.info()
# 这里要把身高体重的数据类型由object改为数值类型
# players.head()
# 使用矢量化字符串方式处理
# players['Height'] = players['Height'].str.replace('cm','')
# players['Weight'] = players['Weight'].str.replace('kg','')
# players.info()
# 替换后，身高和体重仍然是object类型，不是数值型，需要类型转换
# players['Height'] = players['Height'].astype(np.int)
# players['Weight'] = players['Weight'].astype(np.int)
# players.info()

# 使用map和apply
# def handle(item):
    # return int(item.replace('cm',''))
# players['Height'] = players['Height'].map(lambda item:int(item.replace('cm','')))
players['Weight'] = players['Weight'].map(lambda item:int(item.replace('kg','')))
players.info()


#%%
# 运动员身高、体重、评分信息分布
# players['Height'].describe()
# 使用直方图查看分布
# plt.hist(players['Height'])
players['Height'].plot(kind = 'hist',bins=15)
# players['Weight'].plot(kind = 'hist',bins=15)
# players['Rating'].plot(kind = 'hist',bins= 15)
# 核密度图查看数据分布 
players['Height'].plot(kind = 'kde')
# players['Weight'].plot(kind = 'kde')
# players['Rating'].plot(kind = 'kde')


#%%
# 左脚和右脚选手分析  数量上是否存在偏差
# Preffered_Foot
# players['Preffered_Foot'].head(10)
# 需要先进行分组，在分别统计数量
g = players.groupby('Preffered_Foot')
# g.count()
s = g['Preffered_Foot'].count()
# display(type(s))
# 柱状图或者饼图显示左右脚选手数量的差别
# s.plot(kind='bar')
# s.plot(kind = 'pie',autopct = '%.2f')

# 使用Series的value_counts进行简化操作
# 其实上面的操作就是针对‘惯用脚’分组，在统计每组的数量
players['Preffered_Foot'].value_counts().plot(kind = 'barh')

#%%
# 从球员平均分角度，拥有top10评分能力的俱乐部/国家（人数>20）
group = players.groupby('Club')
# display(group['Rating'].mean(),type(group['Rating'].mean()))
# 对Series对象排序
# group['Rating'].mean().sort_values(ascending = False).head(10).plot(kind = 'barh')

# 同时要求人数要大于20人
result = group['Rating'].agg(['mean','count']).sort_values('mean',ascending=False)
result = result[result['count']>20] 
result.head(10).plot(kind='bar')

# top10的国家，只是把club改成nationality

#%%
# 哪个俱乐部最有能力留住球员（5年以上） Club_Joining,Contract_Expriy
r = players[['Club_Joining','Contract_Expiry']]
# 确保有没有合约在2017年之前的球员
r[players['Contract_Expiry']<2017]
# 因为2017年之前没有合约到期，那么效力时间就为2017-签约时间
# map方法可以对Series进行操作，取出假如俱乐部的年份
year = players['Club_Joining'].map(lambda x:x.split('/')[-1])

# display(year,type(year))
# 进行类型转换，转化为数值类型
year = year.astype(np.int64)
# 增加一列数据
players['Work_Year'] = 2017-year
# 筛选数据，小于的5过滤
result = players[players['Work_Year']>=5]
# 结果中存在Free Agents中只有球员，不参与统计，过滤
result = result[result['Club']!='Free Agents']
# 在对于俱乐部分组，统计球员个数
result['Club'].vlaue_counts(ascending = False ).head(10).plot('bar')

#%%
# 球员出生日期分析
# Birth_Date
# players['Birth_Date']
# 全体球员
# 对球员的生日进行切分，扩展为3列
# t = players['Birth_Date'].str.split('/',expand=True)
# 对于月份进行分析，根据月份来分组，统计每格月份对应球员数量，柱状图显示
# t[0].value_counts().sort_values(ascending = True).plot(kind='bar')
# 知名球员（评分在80分以上的）(过滤)
t2 = players[players['Rating']>=80]
t2 = players['Birth_Date'].str.split('/',expand=True)
t2[2].value_counts().sort_values(ascending = True).plot(kind='bar')
#%%
# 身高体重相关性分析   散点图(x,身高，y,体重)，相关系数(协方差，corr)
# 身高和体重的关系
# players.plot(kind = 'scatter',x='Height',y='Weight') 
# 身高和评分的关系
# players.plot(kind = 'scatter',x='Height',y='Rating')

# 相关系数
players['Height'].corr(players['Weight'])

#%%
# 哪些指标对评分的影响比较大（比较相关系数）
# 得到相关系数表（DataFrame）
players.corr()['Rating'].sort_values(ascending= False)

#%%
# 年龄和评分的关系（散点图）
# players.plot(kind='scatter',x='Age',y='Rating')
# 相关系数   
# players['Age'].corr(players['Rating'])
# 利用pandas中的cut方法，可以吧数据切分为离散的区间表示，bins表示几个区间
# 默认区间对应的数值的范围，也可以自定义每个区间的名称（labels）
# pd.cut(players['Age'],bins=4,labels=['少年队','预备队','正式队','老年队'])

# 根据年龄段来分组，再去统计每组年龄的均值，用折线图来描述年龄段和评分之间的关系
players['Age_section'] = pd.cut(players['Age'],bins=4,labels=['少年队','预备队','正式队','老年队'])
players.groupby('Age_section')['Rating'].mean().plot(kind='line',marker='o')

# bins设置区间个数，区间等分，自定义区间范围,列表实现
players['Age_section'] = pd.cut(players['Age'],bins=[10,16,22,23,45],labels=['少年队','预备队','正式队','老年队'])