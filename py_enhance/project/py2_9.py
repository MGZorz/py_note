'''
自定义模块

需求：
    数学四则运算，两个数的加减乘除
'''
# 手动添加全局变量__all__ 之后，from 模块 import *将不在是默认导入所有功能，
# 而是导入__all__列表中所有功能  （python3 环境下不提倡使用）
__all__ = ['add','sub','mul','div']

def add(a,b):
    '''
    加法运算
    :return:两个数的和
    '''
    return  a + b

def sub(a,b):
    '''
    减法运算
    :return:两个数的差
    '''
    return a - b

def mul(a,b):
    '''
     乘法运算
    :return:两个数的积
    '''
    return a*b
def div(a,b):
    '''
    除法运算
    :return:两个数的商
    '''
    return  a / b
if __name__ == '__manin__':
    a = 10
    b = 2
    print('和为：%g' % add(a, b))
    print('差为：%g' % sub(a, b))
    print('积为：%g' % mul(a, b))
    print('商为：%g' % div(a, b))
    # __main__
    print(__name__)
