from matplotlib import pyplot as plt
from DataFromNet import get_price_data


def test6():
    # 获取数据
    dates, nums = get_price_data()
    # 中文字体
    plt.rcParams['font.family'] = ['SimHei']
    x = range(50)
    # 显示刻度
    plt.xticks(x[::2], dates[:50:2], rotation=45)
    # 填充数据
    plt.scatter(x, nums[:50])
    # 显示标题
    plt.title('全国成交土地成交土地均价 (月度数据)')
    # 显示x轴说明
    plt.xlabel('时间频率(月)')
    # 显示y轴说明
    plt.ylabel('元/平方米')
    # 显示图表
    plt.show()




if __name__ == '__main__':
    test6()
