import seaborn as sns
from matplotlib import pyplot as plt
from pandas import Categorical


def test33():
    # 设置图表
    g = sns.FacetGrid(tips, col='time')
    # 填充数据，并绘画
    g.map(plt.hist, 'tip')
    # 展示
    plt.show()


def test34():
    # 设置图表
    g = sns.FacetGrid(tips, col='sex', hue='smoker')
    g.map(plt.scatter, 'total_bill', 'tip', alpha=0.5)
    g.add_legend()  # 增加图例
    plt.show()


def test35():
    # 设置图表
    g = sns.FacetGrid(tips, row='time', col='sex', hue='smoker', margin_titles=True)
    g.map(plt.scatter, 'total_bill', 'tip', alpha=0.5)
    g.add_legend()  # 增加图例
    plt.show()


def test36():
    # 设置图表
    g = sns.FacetGrid(tips, row='time')
    g.map(sns.regplot, 'size', 'total_bill', fit_reg=False, x_jitter=.2)
    plt.show()


def test37():
    # 设置图表
    g = sns.FacetGrid(tips, col='day', aspect=2)
    g.map(sns.barplot, 'sex', 'total_bill')
    plt.show()


def test38():
    row = Categorical(['Fri', 'Sun', 'Sat', 'Thur'])
    # 设置图表
    g = sns.FacetGrid(tips, row='day', aspect=2, row_order=row)
    g.map(sns.boxplot, 'total_bill')
    plt.show()


def test39():
    pal = dict(Yes='green', No='gray')
    # 设置图表
    g = sns.FacetGrid(tips, row='time', col='sex', hue='smoker', palette=pal,margin_titles=True,hue_kws={'marker':['^','v']})
    g.map(plt.scatter, 'total_bill', 'tip', alpha=0.5,edgecolor='blue',s=50,linewidth=0.5)
    g.add_legend()  # 增加图例
    plt.show()


def test40():
    pal = dict(Yes='green', No='gray')
    # 设置图表
    g = sns.FacetGrid(tips, row='time', col='sex', hue='smoker', palette=pal,margin_titles=True,hue_kws={'marker':['^','v']})
    g.map(plt.scatter, 'total_bill', 'tip', alpha=0.5,edgecolor='blue',s=50,linewidth=0.5)
    g.fig.subplots_adjust(wspace=1,hspace=1)
    g.add_legend()  # 增加图例
    plt.show()



def test41():
    pal = dict(Yes='green', No='gray')
    # 设置图表
    g = sns.FacetGrid(tips, row='time', col='sex', hue='smoker', palette=pal,margin_titles=True,hue_kws={'marker':['^','v']})
    g.map(plt.scatter, 'total_bill', 'tip', alpha=0.5,edgecolor='blue',s=50,linewidth=0.5)
    g.set_axis_labels('total','tip')
    g.set(xticks=[10,30,50],yticks=[2,4,6,8,10])
    g.add_legend()  # 增加图例
    plt.show()


if __name__ == '__main__':
    tips = sns.load_dataset('tips')
    # print(tips)
    test41()
