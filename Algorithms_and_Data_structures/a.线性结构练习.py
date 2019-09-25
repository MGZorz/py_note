class Array:
    def __init__(self, size=4):
        self.size = size
        self.length = 0
        self.item = [None] * self.size

    def __getitem__(self, index):
        '''通过索引拿数据'''
        return self.item[index]

    def __setitem__(self, key, value):
        '''添加数据'''
        self.item[key] = value
        self.length += 1

    def __iter__(self):
        '''遍历输出'''
        for i in range(len(self.item)):
            yield self.item[i]

    def show_index(self, value):
        for i in range(self.size):
            if self.item[i] == value:
                index = i
                return index

    def add_first(self, value=None):
        for i in range(self.length, -1, -1):
            self.item[i] = self.item[i - 1]
        self.item[0] = value
        self.length += 1
        if self.enough():
            self.kuo_rong()

    def del_info(self, value=None):
        index = self.show_index(value)
        if index != -1:
            for i in range(index, self.size):
                if i == self.size - 1:
                    self.item[i] = None
                    break
                else:
                    self.item[i] = self.item[i + 1]
            self.length -= 1
        return '无数据'

    def clear(self):
        '''清空'''
        for i in range(self.length):
            self.item[i] = None

    def kuo_rong(self):
        old = self.item
        self.item = [None] * (self.size << 1)
        for i in range(self.size):
            self.item[i] = old[i]
        return self.item

    def enough(self):
        return self.length / float(self.size) > 0.8


if __name__ == '__main__':
    a = Array()
    a.__setitem__(1, 'haha')
    a.__setitem__(0, 'heihei')
    a.__setitem__(2, 'xixi')
    a.add_first('天哪')
    # a.del_info('haha')
    # a.clear()
    # a.kuo_rong()
    for i in a:
        print(i)
