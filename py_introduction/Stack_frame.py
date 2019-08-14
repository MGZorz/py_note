# 测试递归函数的基本原理

def test01():
    print("test01")
    test02()


def test02():
    print("test02")

test01()

def test03(n):
    print("test03:",n)
    if n == 0:
        print("over")

    else:
        test03(n-1)

    print("test03####",n)

test03(9)