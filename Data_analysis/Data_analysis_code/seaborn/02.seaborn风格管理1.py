# pip install seaborn
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns


def test2():
    # 获取数据
    xiao_mi = np.random.randint(50, 100, size=10)
    hua_wei = np.random.randint(50, 100, size=10)
    x = range(10)
    # 启动设置样式
    sns.set_style('whitegrid')
    # 填充数据
    plt.plot(x, xiao_mi)
    plt.plot(x, hua_wei)
    # 展示数据
    plt.show()


def test3():  # 样式：注意要在填充数据之前使用
    # 获取数据
    xiao_mi = np.random.randint(50, 100, size=10)
    hua_wei = np.random.randint(50, 100, size=10)
    x = range(10)
    # 启动设置样式
    sns.set_context()
    sns.set_style('whitegrid')
    plt.subplot(2, 3, 1)
    # 填充数据
    plt.plot(x, xiao_mi)
    # 启动设置样式
    sns.set_style('darkgrid')
    plt.subplot(2, 3, 2)
    plt.plot(x, hua_wei)

    with sns.axes_style('dark'):
        plt.subplot(2, 3, 3)
        plt.plot(x, hua_wei)
    sns.set(style='white')
    plt.subplot(2, 3, 4)
    plt.plot(x, hua_wei)

    sns.set(style='ticks')
    plt.subplot(2, 3, 5)
    plt.plot(x, hua_wei)
    # 展示数据
    plt.show()


def test4():
    sns.set_style('white')
    plt.plot(x, hua_wei)
    # 去轴脊柱 ，注意：在填充数据以后
    sns.despine()
    # 展示数据
    plt.show()


if __name__ == '__main__':
    hua_wei = np.random.randint(50, 100, size=10)
    x = range(10)

    test4()
