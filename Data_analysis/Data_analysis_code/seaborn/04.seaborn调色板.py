from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


def test8():
    palette = sns.color_palette()
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test9():  # 圆形颜色系统 ，模式参数： deep, muted, bright, pastel, dark, colorblind
    # palette = sns.color_palette('dark')
    palette = sns.color_palette('dark', 6)
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test10():
    palette = sns.color_palette('Reds_r', 9)  # 从深到浅
    palette = sns.color_palette('Reds', 9)  # 从浅到深
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test11():
    palette = sns.color_palette('hls')
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test12():
    palette = sns.hls_palette(l=.5, s=.5)
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test13():
    # palette = sns.light_palette('red')
    palette = sns.dark_palette('red')
    # 填充颜色到图表
    sns.palplot(palette)
    plt.show()


def test14():
    plt.plot([0, 1], [0, 1], sns.xkcd_rgb['slate blue'], lw=5)
    plt.plot([0, 1], [0, 2], sns.xkcd_rgb['neon purple'], lw=5)
    plt.plot([0, 1], [0, 3], sns.xkcd_rgb['reddish purple'], lw=5)
    plt.show()


def test15():
    x = range(5, 11)
    plt.bar(x, x, color=sns.color_palette('Reds'))
    plt.show()


def test16():
    data = np.random.normal(size=(20, 8)) + np.arange(8) / 2
    sns.barplot(data=data,palette=sns.color_palette('Blues',10))
    plt.show()
if __name__ == '__main__':
    test16()
