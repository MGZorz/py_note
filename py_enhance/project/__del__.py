# 析构函数__del__()   \垃圾回收机制
# 测试析构方法
class Person :

    def __del__(self):
        print('销毁对象：{0}'.format(self))


p1 = Person()
p2 = Person()
del p2
print('程序结束')
'''先销毁p2（因为del p2 ），然后程序结束p1也销毁了。'''