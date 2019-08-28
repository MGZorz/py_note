#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: polynomial_regression.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

__author__ = 'yasaka'

m = 100
X = 6 * np.random.rand(m, 1) - 3
y = 0.5 * X ** 2 + X + 2 + np.random.randn(m, 1)

X_train = X[:80]
X_test = X[80:]
y_train = y[:80]
y_test = y[80:]

plt.plot(X, y, 'b.')

d = {1: 'g-', 2: 'r+', 10: 'y*'}
for i in d:
    poly_features = PolynomialFeatures(degree=i, include_bias=False)
    X_poly_train = poly_features.fit_transform(X_train)
    X_poly_test = poly_features.fit_transform(X_test)
    print(X[0])
    print(X_poly_train[0])
    # print(X_poly_train[:, 0])

    lin_reg = LinearRegression(fit_intercept=True)
    lin_reg.fit(X_poly_train, y_train)
    # print(lin_reg.intercept_, lin_reg.coef_)

    y_train_predict = lin_reg.predict(X_poly_train)
    y_test_predict = lin_reg.predict(X_poly_test)
    plt.plot(X_poly_train[:, 0], y_train_predict, d[i])

    print(mean_squared_error(y_train, y_train_predict))
    print(mean_squared_error(y_test, y_test_predict))

plt.show()
