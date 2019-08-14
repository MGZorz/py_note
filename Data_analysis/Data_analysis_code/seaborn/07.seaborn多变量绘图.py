from matplotlib import pyplot as plt
import seaborn as sns


def test23():
    sns.stripplot(x='day', y='total_bill', data=data)
    plt.show()


def test24():
    sns.swarmplot(x='day', y='total_bill', data=data)
    plt.show()


def test25():
    sns.swarmplot(x='day', y='total_bill', hue='sex', data=data)
    plt.show()


def test26():
    sns.swarmplot(x='day', y='total_bill', hue='time', data=data)
    plt.show()


def test27():
    sns.boxplot(x='day', y='total_bill', hue='time', data=data)
    plt.show()


def test28():
    # sns.violinplot(x='total_bill', y='day',hue='time',  data=data)
    sns.violinplot(x='day', y='total_bill', hue='sex', data=data, split=True)
    plt.show()


def test29():
    sns.swarmplot(x='day', y='total_bill', data=data,alpha=.5,color='w')

    sns.violinplot(x='day', y='total_bill', data=data, inner=None)

    plt.show()



if __name__ == '__main__':
    # 生成数据
    data = sns.load_dataset('tips')
    test29()
