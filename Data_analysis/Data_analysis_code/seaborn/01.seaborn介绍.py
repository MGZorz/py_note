# pip install seaborn
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def test1():
    # 获取数据
    xiao_mi = np.random.randint(50, 100, size=10)
    hua_wei = np.random.randint(50, 100, size=10)
    x = range(10)
    # 启动设置样式
    sns.set()
    # 填充数据
    plt.plot(x, xiao_mi)
    plt.plot(x, hua_wei)
    # 展示数据
    plt.show()

    # 注意：报错：dateutil 2.5.0 is the minimum required version
    # pip install -U python_dateutil
