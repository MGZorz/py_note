'''
异常的传递：
'''

def text1():
    print('-'*10+'test1开始'+'-'*10)
    #   异常，不正常，Python 解释器遇到无法解释的代码的时候，罢工
    print(aa)
    print('-'*10+'test1结束'+'-'*10)

def text2():
    print('-'*10+'test2开始'+'-'*10)
    text1()
    print('-'*10+'test2结束'+'-'*10)

def text3():
    print('-'*10+'test3开始'+'-'*10)
    # text2()
    try:
        text2()
    except:
        pass
    print('-'*10+'test3结束'+'-'*10)

text3()

