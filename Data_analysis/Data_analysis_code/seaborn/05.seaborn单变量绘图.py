import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def test17():
    # 生成数据
    data = np.random.normal(size=100)
    print(data)
    # 绘画数据
    # sns.distplot(data, kde=False)
    sns.distplot(data, kde=True, bins=20)
    # 显示图表
    plt.show()


def test18():
    data = np.random.multivariate_normal([0, 1], [(1, 0.5), (0.5, 1)], 1000)
    df = pd.DataFrame(data, columns=['x', 'y'])
    sns.jointplot(x='x', y='y', data=df, kind='hex', color='k')
    # print(data)
    plt.show()


def test19():
    iris = sns.load_dataset('iris')
    sns.pairplot(iris)
    plt.show()


if __name__ == '__main__':
    test19()
