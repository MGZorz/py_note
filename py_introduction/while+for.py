# 测试while循环
'''
num = 0
while num <= 10:
    print(num)
    num += 1
'''

# 计算1-100之间数字的累加和。

'''
num1 = 0
sum_all = 0

while num1<=100:
    sum_all = sum_all + num1
    num1 += 1
print("1-100之间数字之和是：",sum_all)
'''

# for循环测试  遍历

for x in list("anskldalkd"):
    print(x*2)

d = {'name':'wang','age':88,'where':'beijing'}
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
    print(x)

for x in range(5):
    print(x)

num = 0
sum_all = 0
for x in range(0,101):
    sum_all=sum_all+num
    num += 1
print(sum_all)


print("**************************")

sum_all = 0
sum_odd = 0 # 奇数和
sum_even = 0 # 偶数和
for x in range(0,101):
    sum_all += x
    if x%2 == 1:
        sum_odd += x
    else:
        sum_even += x
print("1-100累加总和为{0}，奇数和为{1}，偶数和{2}".format(sum_all,sum_odd,sum_even))