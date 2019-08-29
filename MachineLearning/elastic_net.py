#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: elastic_net.py  L1正则和L2正则的混合应用


import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor  #

__author__ = 'MGZorz'

# 构建简单数据集
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

'''
alpha--> α  l1_ratio --> L1正则的比重  fit_intercept --> 是否存在截距，默认存在 normalize --> 标准化开关，默认关闭
'''
#  先对Elastic_Net回归实例化 ,经验一般α都是为0.4的
elastic_net = ElasticNet(alpha=0.4, l1_ratio=0.15)
# 将x,y以矩阵的方式传入，还要一个参数 sample_weight --> 每条测试参数的权重
elastic_net.fit(X, y)
# predict() -->  预测方法，求得返回预测值（Y）
print(elastic_net.predict(1.5))
# 评分函数，将返回一个小于1的得分，可能也会小于0
print(elastic_net.score(X, y, sample_weight=None))

# 方法二：SGDRegressor类
'''
随机梯度下降法   penalty --> 为回归类型（L1回归[LASSO]，L2回归[岭回归]，elasticnet回归）
n_iter -->  迭代次数
'''
# sgd_reg = SGDRegressor(penalty="elasticnet", n_iter=1000)
# sgd_reg.fit(X, y.ravel())
# print(sgd_reg.predict(1.5))
