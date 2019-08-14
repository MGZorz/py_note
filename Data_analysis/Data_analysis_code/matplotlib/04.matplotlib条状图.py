from matplotlib import pyplot as plt
from DataFromNet import get_company_data, get_movie_data


def test7():
    # 获取数据
    addrs, nums = get_company_data()

    # 设置中文
    plt.rcParams['font.family'] = ['SimHei']
    # 设置x轴位置
    x = range(6)
    # 设置标题
    plt.title('2008年私营企业数量')
    # x轴的数据
    plt.xticks(x, addrs)
    # x轴的信息
    plt.xlabel('地区')
    # y轴的信息
    plt.ylabel('户数')

    # 填充数据
    plt.bar(x, nums, color='red', width=0.2)
    # 显示图表
    plt.show()


def test8():
    # 获取数据
    addrs, nums = get_company_data()

    # 设置中文
    plt.rcParams['font.family'] = ['SimHei']
    # 设置x轴位置
    x = range(6)
    # 设置标题
    plt.title('2008年私营企业数量')
    # x轴的数据
    plt.yticks(x, addrs)
    # x轴的信息
    plt.ylabel('地区')
    # y轴的信息
    plt.xlabel('户数')
    # 设置显示bar的值
    for m, n in zip(x, nums):
        plt.text(n + 1000, m, n)
    # 填充数据
    plt.barh(x, nums)
    # 显示图表
    plt.show()


def test9():
    real_names = []

    # 获取数据
    # names, num1 = get_movie_data(-3)
    # names, num2 = get_movie_data(-4)
    # names, num3 = get_movie_data(-5)

    # real_names = names[:3]
    # real_num1 = num1[:3]
    # real_num2 = num2[:3]
    # real_num3 = num3[:3]
    real_names = ['大侦探皮卡丘', '复仇者联盟4：终局之战', '何以为家']

    real_num1 = [8414, 4024, 2088]
    real_num2 = [11526, 5605, 2490]
    real_num3 = [7675, 2863, 1311]
    # print(real_names, real_num1, real_num2, real_num3)
    # 设置中文
    plt.rcParams['font.family'] = ['SimHei']

    plt.title('电影票房前三排名统计（3天）')
    plt.xlabel('天数')
    plt.ylabel('票房数')

    # 设置x轴位置
    x1_pos = list(range(3))
    x2_pos = [i + 0.3 for i in x1_pos]
    x3_pos = [i + 2 * 0.3 for i in x1_pos]

    print(x1_pos, x2_pos, x3_pos)
    # 设置x轴标签
    x_ticks = ['第{}天'.format(i) for i in range(1, 4)]
    plt.xticks(x2_pos, x_ticks)
    # 设置条状图宽度
    width = 0.3
    # 填充数据

    plt.bar(x1_pos, real_num3, width=width,label='大侦探皮卡丘')
    plt.bar(x2_pos, real_num2, width=width,label='复仇者联盟4：终局之战')
    plt.bar(x3_pos, real_num1, width=width,label='何以为家')
    # 显示图例
    plt.legend()
    # 显示图标
    plt.show()


if __name__ == '__main__':
    test9()
