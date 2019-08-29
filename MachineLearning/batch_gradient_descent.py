#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: batch_gradient_descent.py   批量梯度下降法

import numpy as np

__author__ = 'MGZorz'

# 数据集
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

x_b = np.c_[np.ones((100, 1)), X]  # 构造矩阵X_b

learning_rate = 0.001  # 学习率

n_iterations = 1000  # 迭代的次数，但是并不是次数越多越靠近与收敛点

# 这里有一个早停法，可以到制定的程度，停止迭代

m = 100

# 1、初始化θ
theta = np.random.rand(2, 1)
# 4、不会设置阈值（临界值），直接设置超参数，迭代次数，迭代次数到了，我们就认为收敛了
# 超参数：在学习开始之前设置的参数叫超参数，不是通过训练学习得到的参数
for iteration in range(n_iterations):
    # 2、求梯度gradients
    gradients = 1 / m * x_b.T.dot(x_b.dot(theta) - y)
    # Ps: X_b 是一个100行两列的矩阵，dot(theta)是两行一列的矩阵 结果为100行1列的-y(也是100行一列的矩阵) 得到一个误差
    #    .T为矩阵的转置，100行2列的转置为2行100列，[x_b.T 点积乘 dot()]；结果为2行1列的矩阵{g0,g1}, 1/求平均梯度
    # 3、应用公式调整θ值
    theta = theta - learning_rate * gradients

print(theta)
