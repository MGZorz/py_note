from matplotlib import pyplot as plt


def test10():
    # 获取数据
    data = [45, 49, 42, 42, 36, 37, 31, 38, 35, 39, 43, 33, 34, 36, 35, 36, 34, 32, 36, 32, 37, 33, 32, 38, 35]
    # 设置组距
    bin_width = 2

    # 设置分组
    bin_count = int((max(data) - min(data)) / bin_width)
    # 设置x轴标签位置
    x = range(bin_count)
    x_ticks = range(31, 50, 2)
    # 设置x轴标签的值
    plt.xticks(x_ticks)
    # 填充数据
    plt.hist(data, bin_count)
    # 显示图表
    plt.show()


if __name__ == '__main__':
    test10()
