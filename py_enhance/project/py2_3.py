'''
try:

except (异常1，异常2，异常3...) as e :
使用元组存储多个异常的时候，多个异常之间没有顺序要求
也可以把捕获到的异常存储到某个变量中。
'''
a = input('请输入被除数')
b = input('请输入除数')
try:
    a = int(a)
    b = int(b)
    # 求商
    c = a / b
    print('商为：%g'%c)
except (Exception,ValueError,ZeroDivisionError) as e :
    print(type(e))
    #   错误信息
    print(e.args)
    print('遇到异常')