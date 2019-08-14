# 用递归函数，计算阶乘！！

# 5！=4*3*2*1 =
def f(n):

    if n == 1:
        return 1
    else:
        return n*f(n-1)   # 注意要返回值，不返回子没法进行计算
result = f(5)
print(result)
