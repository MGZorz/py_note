from matplotlib import pyplot as plt
import seaborn as sns


def test30():
    # 条形图
    sns.barplot(x="sex", y="survived", hue="class", data=titanic)
    plt.show()
def test31():
    # 点图
    #sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
    sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
                  palette={"male": "g", "female": "m"},
                  markers=["^", "o"], linestyles=["-", "--"])
    plt.show()

def test32():

    #sns.catplot(x="day", y="total_bill", hue="smoker", data=tips)

    # sns.catplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar")
    #
    # sns.catplot(x="day", y="total_bill", hue="smoker",
    #                col="time", data=tips, kind="swarm")
    #
    sns.catplot(x="time", y="total_bill", hue="smoker",
                   col="day", data=tips, kind="box", height=4, aspect=.5)
    plt.show()
if __name__ == '__main__':
    # 生成数据
    titanic = None #'sns.load_dataset('titanic')
    tips = sns.load_dataset('tips')
    # print(titanic)
    test32()
