#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: polynomial_regression.py

import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures  # 多项式回归是放在sklearn中的数据预测的包中，perprocessing  PolynomialFeatures
from sklearn.linear_model import LinearRegression  # 线性回归，放在线性模型中的
from sklearn.metrics import mean_absolute_error  # 数据误差分析

__author__ = 'MGZorz'

m = 100
X = 6 * np.random.rand(m, 1) - 3  # 构建数量集X，范围在【-3,3】
Y = 0.5 * X ** 2 + X + 2 + np.random.rand(m, 1)  # 真实集Y , 默认数0.5x^2 +x +2 +误差

# 把X数量集分为两部分 x_train和x_test  ,真实集Y同样也分为两部分
X_train = X[:80]
X_test = X[80:]
Y_train = Y[:80]
Y_test = Y[80:]

# 先对X,Y画一条线性线
plt.plot(X, Y, 'b.')  # 显示是一个类似于耐克商标的图像

d = {1: 'g-', 2: 'r+', 10: 'y*'}  # 固定升阶的阶数，和对应数据点的颜色样式
for i in d:
    poly_features = PolynomialFeatures(degree=i, include_bias=False)
    # 构造特征，degree为多项式的次数，include_bias 默认为True,表示有木有0次项，也就是全为1的一列数据集
    x_poly_train = poly_features.fit_transform(X_train)  # 把非线性的数据转化为线性的数据。
    x_poly_test = poly_features.fit_transform(X_test)

    lin_reg = LinearRegression(fit_intercept=True)  # 构建线性回归模型。
    lin_reg.fit(x_poly_train, Y_train)  # 训练找寻这两者之间的线性关系  lin_reg
    y_train_predict = lin_reg.predict(x_poly_train)  # 通过线性关系求出基于x_poly_train数据得到的y的值
    y_test_predict = lin_reg.predict(x_poly_test)  # 通过线性关系求出基于x_poly_test数据得到的y的值
    plt.plot(x_poly_train[:, 0], y_train_predict, d[i])

    # 查看误差的情况
    print(mean_absolute_error(y_train_predict, Y_train))  # 通过模型得到的数值和训练的数值之间的误差
    print(mean_absolute_error(y_test_predict, Y_test))  # 通过模型预测的数值和测试集中数据之间的误差

plt.show()
