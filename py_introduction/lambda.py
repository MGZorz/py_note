f = lambda a,b,c:a*b*c

def  test01(a,b,c):
    return a*b*c

print(test01(2,3,4))
print(f(2,3,4))

# lambda + 函数参数 ：表达式（函数体）

g = [lambda a:a*9,lambda b:b**2,lambda c:c]
print(g[0](6),g[1](8),g[2](3))
