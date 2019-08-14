'''
深浅复制:
    1、浅复制:复制一个新的对象，但是位置储存于原对象相同
        copy.copy()
    2、深复制：复制新的对象，原对象也复制一次，全部都换掉
        copy.deepcopy()
    区别和联系：
    1、联系：
        复制一个新的备份出来
    2、区别：
        对于普通的对象没有区别
        如果目标对象是复合对象<一个对象的成员变量还是对象>的话，有区别
            深复制递归复制
            浅复制，只赋值直接对象
            list1 =[1,2,3]      普通对象

            list2 = [[1,2],[1,2,3]]     复合对象

'''
import copy

# list1 = [1,2,3]
# # 浅复制
# list2 = copy.copy(list1)
# # 深复制
# list3 = copy.deepcopy(list1)
# print(list2)
# print(list2 is list1)
# print(id(list2))
# print('_'*50)
# print(list3)
# print(list3 is list1)
# print(id(list3))

list1 = [1,2]
list2 = [3,4]
# 复合对象
list3 = [list1,list2]
#浅复制
list4 = copy.copy(list3)
#深复制
list5 = copy.deepcopy(list3)