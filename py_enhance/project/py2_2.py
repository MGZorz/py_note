'''
try:

except 异常1：
except 异常2：
except 异常3：
...
多个异常之间的顺序要求：
      （子类在前父类在后）
'''
a = input('请输入被除数')
b = input('请输入除数')
try:
    a = int(a)
    b = int(b)
    # 求商
    c = a / b
    print('商为：%g'%c)
except ValueError:
    print('数据类型有误')
except ZeroDivisionError:
    print('除数不能为0')

# 父类异常、考虑不到的异常
except Exception:
    print('其他异常')