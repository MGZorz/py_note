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
                del node.next
                break

    def remove_first(self):  # 删除最开始的那个 ,这里不光是删除，记得要把指针也该成新的第一个
        node = self.root.next
        self.root.next = node.next
        del self.root.next

    def remove(self, value):  # 通过value删除指定的node
        for node in self.__iter__():  # 遍历其中所有的对象
            if node.next.value == value:  # 找到value对应的那个
                tem_node = node.next
                node.next = tem_node.next  # 更改指向
                del tem_node
                break


if __name__ == '__main__':
    link = LinkList()
    link.append('李白')
    link.append('杜甫')
    link.append('白居易')
    for node in link:
        print(node.value)
    print('-' * 30)
    link.append_first('王安石')
    for node in link:
        print(node.value)
    print('-' * 30)
    link.remove_end()
    for node in link:
        print(node.value)
    print('-' * 30)
    link.remove('李白')
    for node in link:
        print(node.value)
