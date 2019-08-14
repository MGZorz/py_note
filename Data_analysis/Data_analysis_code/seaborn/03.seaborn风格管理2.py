from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


def test5():
    # 设置线条风格
    sns.set_context('poster')
    plt.plot(x, hua_wei)
    plt.show()

def test6():
    # 设置线条风格
    sns.set(context='poster')
    plt.plot(x, hua_wei)
    plt.show()

def test7():
    # 设置线条风格
    sns.set_context('poster',font_scale=0.8, rc={"lines.linewidth": 5})
    plt.plot(x, hua_wei)
    plt.show()
    current_palette = sns.color_palette('deep', 8)

if __name__ == '__main__':
    hua_wei = np.random.randint(50, 100, size=10)
    x = range(10)
    test7()
