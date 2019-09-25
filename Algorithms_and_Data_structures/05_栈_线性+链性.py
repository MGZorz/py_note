'''栈 ---- 线性'''


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

    def add_info(self, value=None):  # 增加首项
        for i in range(self.length, -1, -1):  # 这里反向挪移
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


class StacK(Array):
    '''LOFI'''

    def __init__(self, maxsize=4):
        Array.__init__(self)
        self.push_num = 0  # 输入数据
        self.pop_num = 0  # 拿取数据
        self.maxsize = maxsize

    def pop(self):
        if self.pop_num < 0:  # 判断pop_num是否小于0 ，小于0就证明没数据了
            return '无数据'
        for num in range(self.pop_num, -1, -1):  # 不小于零就从大到小遍历打印
            data = self.__getitem__(num)
            self.pop_num -= 1
            return data

    def push(self, value):
        self.__setitem__(self.push_num, value)
        self.push_num += 1
        self.pop_num = self.push_num - 1


''' 栈 -----  链性  '''


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkList:
    def __init__(self, value=None):
        self.root = Node()
        self.end = None
        self.length = 0

    def __iter__(self):
        current = self.root.next
        while current is not self.end:
            yield current
            current = current.next
        yield current

    def append(self, value):
        '''添加数据'''
        node = Node(value)  # 新建一个node对象
        if self.root.next == None:  # 如果root的指向是None，也就是没有下一个
            self.root.next = node  # 那么就把node作为下一个
        else:
            self.end.next = node  # 如果root的下一个指向有数，那么把node添加下一个
        self.end = node  # 然后结束也就是node
        self.length += 1

    def append_first(self, value):
        node = Node(value)
        if self.end is None:  # 如果下一个None
            self.root.next = node  # 那么node就为下一个
        else:
            tem_node = self.root.next  # 如果下一个不为None , 那么要做的是：把下一个改为node ,并且要把root的指向改为node,node的指向为原来root的下一个
            self.root.next = node  # 先把root的指向更改成node
            node.next = tem_node  # 在把node的指向改为原来的root的下一个
        self.length += 1

    def remove_end(self):  # 删除最后的那个
        for node in self.__iter__():  # 遍历其中的对象
            if node.next == self.end:  # 如果node.next的指向是最后的，那么就把最后的变为node，并且删除原来最后的
                self.end = node
                data = node.next
                del node.next
                return data

    def remove_first(self):  # 删除最开始的那个 ,这里不光是删除，记得要把指针也该成新的第一个
        node = self.root.next
        self.root.next = node.next
        return node.value

    def remove(self, value):  # 通过value删除指定的node
        for node in self.__iter__():  # 遍历其中所有的对象
            if node.next.value == value:  # 找到value对应的那个
                tem_node = node.next
                node.next = tem_node.next  # 更改指向
                del tem_node
                break


class Stack:
    def __init__(self, maxsize=4):
        self.__item = LinkList()
        self.push_num = 0
        self.pop_num = 0

    def pop(self):
        if self.push_num == 1:
            data = self.__item.end
        elif self.push_num < 1:
            return '无数据'
        else:
            data = self.__item.remove_end()
        self.push_num -= 1
        return data.value

    def push(self, value):  # 添加
        self.__item.append(value)
        self.push_num += 1


if __name__ == '__main__':
    stack1 = StacK()
    stack1.push('李白')
    stack1.push('杜甫')
    stack1.push('王安石')
    stack1.push('白居易')
    # 顶掉操作未实现
    # stack.push('苏轼')

    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())

    '''LIFO'''
    stack2 = Stack()
    stack2.push('李白')
    stack2.push('杜甫')
    stack2.push('苏轼')
    # stack.push('白居易')
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
    print(stack2.pop())
