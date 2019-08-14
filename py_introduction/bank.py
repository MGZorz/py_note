'''
需求：
    1、编写一个银行卡类，具有账号，人名与余额属性。
    2、编写提款机类，接收一张银行卡，并且具有存款，提款，查询余额，转账功能。

分解：
    1、银行卡类：
        1、print 卡号名字和余额
        2、存款之后，余额+取款之后余额+转账之后余额
        3、异常情况:
            余额不能小于0
    2、提款机类
        1、插卡，查询，存款，取款，转账，退卡
'''
# 余额不能小于0
class MoneyException(Exception):
    def __init__(self):
        super().__init__()
        self.errMsg = '此为储蓄卡不能透支使用'

# 银行卡类
class Bankcard():
    def __init__(self,id,name,money):
        self.id = id
        self.name = name
        self.set_money(money)

    # 显示余额
    def show(self):
        print('账号：{0}，姓名：{1}，余额：{2}'.format(self.id, self.name, self.money))

    # 设置余额
    def set_money(self,money):
        if money >= 0 :
            self.money = money
        else:
            # 抛出异常(余额异常）
            raise MoneyException()
    # 获取余额
    def get_money(self):
        return self.money


    #存款
    def put_in(self,money):
        self.money += money
        print('存款成功，余额为：{0}'.format(self.money))


    #取款
    def put_out(self,money):
        if self.money>=money:
            self.money -= money
            print('取款成功，余额为：{0}'.format(self.money))
        else:
            raise MoneyException()

    #转账
    def turn(self,card2,money):
        if self.money>=money:
            self.money -= money
            card2.money += money
            print('转账成功，您的余额为：{0}'.format(self.money))
        else:
            raise MoneyException()

# 提款机类
class ATM():
    def __init__(self,id,card=None):
        self.id = id
        self.card = None

    #   插卡
    def insert_card(self,card):
        self.card = card


    #   余额查询
    def balance(self):
        return self.card.get_money()

    #   取款
    def getout_money(self,card,money):
        if card.money >= money:
            card.money -= money
            print('您好，账户：{0}，您的余额为：{1}'.format(card.name, card.money))
        else:
            raise MoneyException()

    #   存款
    def getin_money(self,card,money):
        card.money += money
        print('您好，账户：{0}，您的余额为：{1}'.format(card.name, card.money))
    #   转账
    def turn(self,card,card2,money):
        if card.money <= money:
            card.money -= money
            card2.money += money
            print('您好，转账成功，账户：{0}，您的余额为：{1}'.format(card.name, card.money))
            print('您好，转账成功，账户：{0}，您的余额为：{1}'.format(card2.name, card2.money))
        else:
            raise MoneyException

try:
    c1 = Bankcard('123', '??', 300)
    # c1.show()
    # c1.put_out(300)
    # c1.put_in(300)
    c2 = Bankcard('456', '!!', 600)
    # c1.turn(c2,300)
    atm = ATM('ICBC001')
    atm.insert_card(c1)
    print(atm.balance())
    atm.getin_money(c1,500)
    atm.getout_money(c1,600)
    atm.turn(c1,c2,200)

except MoneyException as e :
    print(e.errMsg)


