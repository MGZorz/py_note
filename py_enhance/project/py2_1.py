'''
1、异常：
    不正常
2、案例：
    需求： 输入被除数与除数，求商，并打印结果
    a,b,c

问题：
    1、str->int 如果str不是纯数字的问题
        ValueError: invalid literal for int() with base 10: 'a'
    2、ZeroDivisionError: division by zero
解决方案：
    1、使用if-else 增加相关的容错处理
        业务核心：
            业务偏移
    2、异常处理方案：
        try：
            可能出现问题的代码
        except：
            如果出现问题，会执行的代码块


'''
a = input('请输入被除数')
b = input('请输入除数')
# str -> int
# 如果字符串a与字符串b全部都为纯数字组成，在进行转化，和后续的操作。
# 原始版本
# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)
#     # 求商
#     if b != 0:
#         c = a / b
#         print('商为：%g' % c)
#     else:
#         print('除数不能为零，操作有误')
# else:
#     print('输入类型有误')

try:
    a = int(a)
    b = int(b)
    # 求商
    c = a / b
    print('商为：%g'%c)
except:
    print('输入类型有误/除数不能为0')
