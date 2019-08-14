from matplotlib import pyplot as plt
import seaborn as sns


def test20():
    # print(data)
    # 填充数据
    sns.regplot(x='total_bill', y='tip', data=data)
    # 显示图表
    plt.show()


def test21():
    # print(data)
    # 填充数据
    sns.lmplot(x='total_bill', y='tip', data=data)
    # 显示图表
    plt.show()


def test22():
    # sns.regplot(x='size',y='tip',data=data)
    sns.regplot(x='size', y='tip', data=data, x_jitter=0.05)
    plt.show()


if __name__ == '__main__':
    # 生成数据
    data = sns.load_dataset('tips')
    test22()
