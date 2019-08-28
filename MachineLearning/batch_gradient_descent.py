#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: batch_gradient_descent.py   批量梯度下降法

import numpy as np

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
# print(X)
y = 4 + 3 * X + np.random.randn(100, 1)
# print(y)
# 矩阵
X_b = np.c_[np.ones((100, 1)), X]
# print(X_b)

# 学习率
learning_rate = 0.0001
# 迭代的次数 并不是次数越多越靠近期望。
n_iterations = 1000000
# Early stopping 早停法
m = 100

# 1，初始化theta，w0...wn
theta = np.random.randn(2, 1)

# 4，不会设置阈值（临界值），直接设置超参数，迭代次数，迭代次数到了，我们就认为收敛了
# 超参数：在学习开始之前设置的参数叫超参数，不是通过训练学习得到的参数
for iteration in range(n_iterations):
    # 2，接着求梯度gradient
    gradients = 1 / m * X_b.T.dot(X_b.dot(theta) - y)  # .T为矩阵的转置
    # PS : X_b 是一个100行两列的矩阵，dot(theta)是两行一列的矩阵 结果为100行1列的-y(也是100行一列的矩阵) 得到一个误差
    # .T为矩阵的转置，100行2列的转置为2行100列，点积乘 dot(100行1列的矩阵)  结果为2行1列的矩阵{g0,g1}, 1/求平均，梯度
    # 3，应用公式调整theta值，theta_t + 1 = theta_t - grad * learning_rate
    theta = theta - learning_rate * gradients

print(theta)
