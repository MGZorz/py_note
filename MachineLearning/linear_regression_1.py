#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: linear_regression_1.py

import numpy as np
from sklearn.linear_model import LinearRegression

__author__ = 'MGZorz'

X1 = 2 * np.random.rand(100, 1)
X2 = 2 * np.random.rand(100, 1)
X = np.c_[X1, X2]
y = 4 + 3 * X1 + 5 * X2 + np.random.randn(100, 1)

lin_reg = LinearRegression()
lin_reg.fit(X, y)
print(lin_reg.intercept_, lin_reg.coef_)

X_new = np.array([[0, 0, 0], [2, 1, 3]])
print(lin_reg.predict(X_new))
