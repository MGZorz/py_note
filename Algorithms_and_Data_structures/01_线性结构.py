class Array:
    def __init__(self, size=4):
        self.__size = size  # 先规定大小（为4）
        self.__item = [None] * size  # 默认全为None
        self.length = 0

    def __getitem__(self, index):
        '''如果在类中定义了这种方法，那么他的实例对象（P）就可以P[key]取值'''
        return self.__item[index]

    def __setitem__(self, key, value):
        '''该方法应该按一定的方式存储和key相关的value。在设置类实例属性时自动调用的'''
        self.__item[key] = value
        self.length += 1

    def __iter__(self):
        for i in range(len(self.__item)):
            yield self.__item[i]

    def clear(self):
        '''清空全部信息'''
        for i in range(self.__size):
            self.__item[i] = None

    def del_info(self, value=None):
        index = self.show_index(value)  # 找到想要删除value的index
        if index != -1:  # 如果index为-1 ，则一定是没有这个的
            for i in range(index, self.__size):  # 遍历索引值到容量
                if i == self.__size - 1:  # 如果是最后的那个
                    self.__item[i] = None  # 那么直接给赋值就OK了 ，并且跳出这个遍历
                    break
                self.__item[i] = self.__item[i + 1]  # 如果不是最后的那个，那么后面的全部都要往前挪一个
            self.length -= 1
        else:
            return '没有此值'

    def show_index(self, value):
        '''显示索引'''
        index = -1
        for i in range(self.__size):
            if self.__item[i] == value:
                index = i
        return index

    def add_info(self, value=None):   # 增加首项
        for i in range(self.length, -1, -1):   # 这里反向挪移
            self.__item[i] = self.__item[i - 1]
        self.__item[0] = value
        if self.enough():
            self.kuo_rong()

    def kuo_rong(self):
        old = self.__item
        self.__item = [None] * (self.__size << 1)
        for i in range(self.__size):
            self.__item[i] = old[i]
        return self.__item

    def enough(self):
        return self.length / float(self.__size) > 0.8


if __name__ == '__main__':
    a = Array()
    a[0] = '张飞'
    a[1] = '刘备'
    a[2] = '关羽'
    print(a[0])
    print(a[1])
    print(a[2])
    print('-------- 遍历 ------------')
    for i in a:
        print(i)
    # print('--------清空------------')
    # a.clear()
    # for i in a:
    #     print(i)
    # print('---------- 删除指定元素 ---------')
    # a.del_info('刘备')
    # for i in a:
    #     print(i)
    print('---------- 增加元素 ------------')
    a.add_info(value='诸葛亮')
    for i in a:
        print(i)
    print('------------ 扩容 ----------------')
    a.kuo_rong()
    for i in a:
        print(i)
