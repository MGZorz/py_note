# 第一题
# 打印斐波那契数列数列前n项和
# 循环的方法
def f(n):
    if n == 1 or n ==2:
        return 1
    else:
        for i in range(2:n):
            return f(n-1)+f(n-2)
print(f(9))



