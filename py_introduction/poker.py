'''
    需求：
    设计单张扑克牌类Card，具有花色，牌面与具体值。同时设计整副扑克牌类Cards，具有52张牌。

    红桃、黑桃、方片、草花  2345678910JQKA  ♥♠♦♣

    设计一个发牌的函数，可以任意发出三张牌。对任意三张牌断定牌的类型。
    类型包括：
            三条：三张牌value一样
            一对：两张value一样
            顺子：三张牌挨着
            同花：三张牌type一样
            同花顺：挨着，类型一样
            其余都是散牌

    分解：
        1、规定花色，和值
        2、判断是否为上述的情况

'''
# 异常类
class TypeError(Exception):
    def __init__(self):
        super().__init__()
        self.errMsg = '牌太小了，不满足任意一种情况'
# 卡牌
class Card():
    def __init__(self,color,value):
        self.color = color
        self.value = value

    #    输出的是字符串+数字，不能拼接在一起，利用函数__str__()以及format返回字符串
    def __str__(self):
        return '{}{}'.format(self.color,self.value)
    # 花色和数字是一对一的关系
    def make(self):
        print('花色：{0}，数值：{1}'.format(self.color,self.value))

# 一副牌
import random
class Cards():

    def __init__(self):
        #   全部的牌
        self.all_card = []
        #   抽出来的三张
        self.t_card = []
        #   花色
        color = '♥♠♦♣'
        #   数值
        value = list(range(2,11)) + list('JQKA')
        for i in color:
            for j in value:
                c = Card(i,j)
                #   把生成的卡片放在all_card中。
                self.all_card.append(c)


    def fa_pai(self):
        for i in range(3):
            self.t_card = random.sample(self.all_card,3)
            # for card in self.t_card:
            #     # end =','用逗号，隔开
            #     print(card,end=',')
            # #   换行
            # print()

    # 判断函数
    def choose(self):
        c1 = self.t_card[0]
        c2 = self.t_card[1]
        c3 = self.t_card[2]
        if c1.value == c2.value and c2.value == c3.value :
            print('三条！')
        elif c1.value == c2.value and c2.value != c3.value:
            print('对儿')
        elif c1.value == c2.value + 1 == c3.value + 2 or c1.value == c2.value - 1 == c3.value - 2:
            print('顺子')
        elif c1.color == c2.color and c2.color == c3.color:
            print('同花')
        elif c1.color == c2.color == c3.color and c1.value == c2.value+1 == c3.value+2 :
            print('同花顺')
        else :
            raise TypeError()
    # 显示所有的牌
    def show_all(self):
        for c in self.t_card:
            print(c)
        print()


try:
    cards = Cards()
    cards.fa_pai()
    cards.choose()
    cards.show_all()
except TypeError as e :
    print(e.errMsg)







