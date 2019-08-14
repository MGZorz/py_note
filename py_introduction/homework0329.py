# 第一题
# num = []
# for i in range(10):
#     for m in range(10):
#         for n in range(10):
#             s1 = i*100+m*10+n
#             s2 = i**3+m**3+n**3
#             if s1 == s2 and s1 > 100:
#                 num.append(s1)
# print('水仙花数如下：\n',num)

# 第二题
# text = 'azbcabbd'
# list_text = list(text)  # 先把字符串转化为列表，方便进行字母的操作。
#
# for i in list_text:     # 遍历在列表中的所有元素
#     if list_text.count(i) > 1:          # 如果元素的个数大于1，就删除
#         list_text.remove(i)
# print(''.join(list_text))   # 通过创建空字符串，把列表放进去。


# 第三题
# url_all = ' http://news.gzcc.cn/html/xiaoyuanxinwen/4.html'
# print(url_all[1:])  # 去掉空格
#
# print(url_all[8:])  #  去掉http://前缀。
#
# print(url_all[:42],'还要输出',url_all[-6])
#
# print(url_all.count('n'))  #  显示在字符串中n的个数
#
# print(url_all.split('/')) # 通过'/'来分割字符串


# 第四题
# while True:
#     num = input("请输入一个5位数")
#     if num[0] == num[4] and num [1] ==num [3]:
#         print("恭喜你，你输入这个是个回文数啊")
#         break
#     else:
#         print("很可惜，不是回文数哦~,请重新输入")

# 第五题
# num = list(input("请输入数字一连串数字，以空格隔开，最后以stop结束").split( ))
# num_int = []
# if 'stop' in num :
#     num.remove('stop')
#     for i in num:
#         num_int.append(int(i))
#     num_sum = sum(num_int)
#     average = num_sum/len(num_int)
#     print('平均值是{0}'.format(average))

# 第六题
# s2 = 'hellodladfljdkfj'
# s1 = 'hllz'
# num = []
# for i in range(4):
#     num = s2.count(s1[i])
#     print(num,end='\t')

# 第七题

# week_day =[]
# def f(a,n):    # a:今天周几，n:n天之后是周几
#     week = ['周一','周二','周三','周四','周五','周六','周日']
#     print('今天是{0}'.format(week[a-1]))
#     # 周三   1天后是周四、两天后是周五、三天厚实周六
#     for i in range(8):
#         week_day.append(i)
#     print('{0}天后是{1}'.format(n,week[a-1+n//7]))


# 第八题
# def f(n):
#     if ' ' in n:
#         return print('调用字有空格哦')
#     else:
#         return print('调用字符没有空格啊')
# f('4    465465')

# 第九题
# def f(n):
#     if len(n)>2:
#         return  print(n[:2],'其他的不符合要求')
#     else:
#         return  print('不符合要求')

# 第十题
#
# def f(n):
#     int_count = 0  # 数字的字符个数
#     str_Count = 0   #大写字母的字符个数
#     str_count = 0   # 小写字母的字符个数
#     other_count = 0 # 其他字符的个数
#     for i in n:
#         if i.isdigit(): #如果是数字。
#             int_count += 1
#         elif i.isupper():   # 如果是大写字没有
#             str_Count += 1
#         elif i .islower():
#             str_count += 1
#         else :
#             other_count += 1
#     return print('您输入的字符中，大写字母有{}个，小写字母有{}个，数字有{}个，其他字符有{}个'
#                  .format(str_Count,str_count,int_count,other_count))
#
# f('asdasdasdQQQasdasd@@@@235112  de asDER')

# 第十一题
# def f(n):
#     nam = list(input("请输入学生姓名，用空格隔开，stop结束").split( ))
#     score = list(input("请输入各自的成绩，用空格隔开，stop结束").split( ))
#     if 'stop' in nam and 'stop' in score:
#         nam.remove('stop')
#         score.remove('stop')
#     a = ['name','score']
#     b = [nam,score]
#     dic = dict(zip(a,b))

ss = {"tom":60,"kate":100,"jerry":80,"lily":89,"luly":100}
name = list(ss.keys())
score = list(ss.values())
for i in score:
    if i == max(score):
        ss.get(name[i])
        print("[1]")

