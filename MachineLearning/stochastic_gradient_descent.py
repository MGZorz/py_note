#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: stochastic_gradient_descent.py  随机梯度下降法


import numpy as np

__author__ = 'yasaka'

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]
print(X_b)

n_epochs = 1000
t0, t1 = 5, 500  # 超参数

m = 100


def learning_schedule(t):
    # 控制学习率跟随迭代的次数增加越来越小
    return t0 / (t + t1)


theta = np.random.randn(2, 1)

for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(m)  # 随机生成索引号
        xi = X_b[random_index:random_index + 1]  # 根据随机生成的索引号，利用切片，取出X_b矩阵中的那一行数据
        yi = y[random_index:random_index + 1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)  # 梯度下降公式 求梯度（gradients）
        learning_rate = learning_schedule(epoch * m + i)  # 调用learning_schedule函数使得学习率随着迭代次数的增加而减小
        theta = theta - learning_rate * gradients  # 谁他 - 学习律*梯度

print(theta)
