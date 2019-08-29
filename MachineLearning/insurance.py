#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: insurance.py  保险数据分析

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures  # 多项式回归
from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn.metrics import mean_absolute_error  # 误差分析

__author__ = 'MGZorz'

data = pd.read_csv('./insurance.csv')

'''首先先要对数据本身进行简单的操作筛选'''
# print(data.describe())
# data_count = data['age'].value_counts()
# print(data_count)
# data_count[:10].plot(kind='bar')
# plt.show()
# plt.savefig('./temp')


reg = LinearRegression()
x = data[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
y = data['charges']

# 把x，y的数据转化为数字类型，也就是num
x = x.apply(pd.to_numeric, errors='coerce')
y = y.apply(pd.to_numeric, errors='coerce')

x.fillna(0, inplace=True)  # 缺失值处理，把缺失的值全部用0代替
y.fillna(0, inplace=True)

# 留出法评估
x_train = x[:910]
x_test = x[910:]
y_train = y[:910]
y_test = y[910:]

# 开始对其进行分析了
poly_features = PolynomialFeatures(degree=3, include_bias=False)
# 把x的真实数据添加特征使其变成线性数据
X_train_poly = poly_features.fit_transform(x_train)
X_test_poly = poly_features.fit_transform(x_test)

# 训练过程
reg.fit(X_train_poly, y_train)
y_train_predict = reg.predict(X_train_poly)  # 根据训练出来的模型得到模型相对应的y的值
y_test_predict = reg.predict(X_test_poly)

plt.plot(x['age'], y, 'b.')

plt.plot(X_train_poly[:, 0], y_train_predict, 'r.')
print(mean_absolute_error(y_train_predict, y_train))
print(mean_absolute_error(y_test_predict, y_test))

plt.show()
