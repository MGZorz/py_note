
# 第2题：输入一个三位正整数，输出该数值的百位，十位与个位。

a = "897"
print("百位："+a[0]+",十位："+a[1]+",个位："+a[2]+"。")

# 第3题：输入一个三位正整数，分别输入个位、十位、百位

import time
a = 94241
minutes = a/60
hours = minutes/60
minute = int(minutes)
hour = int(hours)
print("总共是"+str(a)+"秒，折合成分钟是"+str(minute)+"分钟，折合成小时是"+str(hour)+"小时。")


('''s1 = 72 
s2 = 85 
r = s2/s1 
a = "我是{0}，我期末成绩的提升率为{1:.1%}"
a.format("小明"，r)''')
