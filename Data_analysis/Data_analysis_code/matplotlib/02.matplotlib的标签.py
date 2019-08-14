from matplotlib import pyplot as plt
import matplotlib


def test1():  # 基本入门
    # 构造数据
    info = [10, 11, 10, 9, 3, 6, 8, 5, 7, 8, 12, 11]

    x = range(0, 12)
    x_ticks = ['{}月'.format(i) for i in range(1, 13)]
    # 引入字体文件
    font1 = matplotlib.font_manager.FontProperties(fname='SimHei.ttf')
    # 设置x轴的标签
    plt.xticks(x, x_ticks, fontproperties=font1)
    plt.plot(x, info)
    plt.show()


def test2():  # 设置中文
    # 查看系统支持的字体
    # a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
    # for i in a:
    #     print(i)

    # 构造数据
    info = [10, 11, 10, 9, 3, 6, 8, 5, 7, 8, 12, 11]
    x = range(0, 12)
    x_ticks = ['{}月'.format(i) for i in range(1, 13)]
    # 设置plt的字体
    plt.rcParams['font.family'] = ['SimHei']
    # 设置x轴的标签
    plt.xticks(x, x_ticks, rotation=45)
    plt.plot(x, info)
    plt.show()


def test3():  # 设置图片信息
    # 构造数据
    info = [10, 11, 10, 9, 3, 6, 8, 5, 7, 8, 12, 11]
    x = range(0, 12)
    x_ticks = ['{}月'.format(i) for i in range(1, 13)]
    # 设置plt的字体
    plt.rcParams['font.family'] = ['SimHei']
    # 设置x轴的标签
    plt.xticks(x, x_ticks, rotation=45)
    plt.plot(x, info)
    # 设置图标名称
    plt.title('某手机年销售数据统计表(XXXX年)')
    # 设置X轴说明
    plt.xlabel('月份')
    # 设置Y轴说明
    plt.ylabel('销量(万)')
    plt.show()


def test4():  # 绘画多数据与图例
    # 构造数据
    max_temperature = [26, 30, 31, 32, 33]
    min_temperature = [12, 16, 16, 17, 18]

    x = range(5)
    plt.rcParams['font.family'] = ['SimHei']
    x_ticks = ['星期{}'.format(i) for i in range(1, 6)]
    plt.title('某年某周第N周的温度')
    plt.xlabel('周')
    plt.ylabel('温度：单位(℃)')
    # 设置x轴标签
    plt.xticks(x, x_ticks)
    # 填充数据
    plt.plot(x, max_temperature, label='最高温')
    plt.plot(x, min_temperature, label='最低温')
    # 显示图例
    plt.legend(loc=2)
    # 绘画
    plt.show()


def test5():  # 绘画表格细节
    # 构造数据
    max_temperature = [26, 30, 31, 32, 33]
    min_temperature = [12, 16, 16, 17, 18]

    x = range(5)
    plt.rcParams['font.family'] = ['SimHei']

    x_ticks = ['星期{}'.format(i) for i in range(1, 6)]
    plt.title('某年某周第N周的温度')
    plt.xlabel('周')
    plt.ylabel('温度：单位(℃)')
    # 设置表格的标尺
    plt.tick_params(top=False, right=False, left=False, bottom=False)
    # 设置网络表格
    plt.grid(alpha=0.2)  # 透明度值 0-1之间
    # 设置x轴标签
    plt.xticks(x, x_ticks)
    # 设置y轴标签
    y = range(10, 35, 2)
    plt.yticks(y)

    fig, ax = plt.subplots()
    # 取消边框
    for key, spine in ax.spines.items():
        # 'left', 'right', 'bottom', 'top'
        if key == 'right' or key == 'top':
            spine.set_visible(False)

    # 设置RGB颜色
    c1 =(70/255,130/255,180/255)
    c2 =(0/255,255/255,0/255)
    # 填充数据
    plt.plot(x, max_temperature, label='最高温',linewidth=5,c=c2)
    plt.plot(x, min_temperature, label='最低温',linewidth=5,c='m')
    # 显示图例
    plt.legend(loc=2)
    # 绘画
    plt.show()





if __name__ == '__main__':
    test5()
