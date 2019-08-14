import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


def test42():
    # 绘画热力图
    sns.heatmap(data, vmin=0.2, vmax=0.5)
    # 显示
    plt.show()


def test43():
    # 绘画热力图
    sns.heatmap(data, center=0)
    # 显示
    plt.show()


def test44():
    # 转换数据
    data = flights.pivot('month', 'year', 'passengers')
    # print(data)
    sns.heatmap(data, annot=True, fmt='d', linewidths=0.5)
    plt.show()


def test45():
    # 转换数据
    data = flights.pivot('month', 'year', 'passengers')
    # print(data)
    sns.heatmap(data, annot=True, fmt='d', linewidths=0.5, cmap='BuGn')
    plt.show()


def test46():
    # 转换数据
    data = flights.pivot('month', 'year', 'passengers')
    # print(data)
    sns.heatmap(data, annot=True, fmt='d', linewidths=0.5, cmap='BuGn',cbar=False)
    plt.show()
if __name__ == '__main__':
    data = np.random.randn(3, 3)
    # print(data)
    flights = sns.load_dataset('flights')
    # print(flights.head())
    # test43()
    # test44()
    # test45()
    test46()
