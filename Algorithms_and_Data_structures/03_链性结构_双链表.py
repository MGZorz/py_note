class Node():
    def __init__(self, value=None, next=None, top=None):
        self.value = value
        self.next = next
        self.top = top


class LinkList():
    def __init__(self, length=0):
        self.root = Node()
        self.end = None
        self.length = length

    def __iter__(self):
        current = self.root.next
        while current is not self.end:
            yield current
            current = current.next
        yield current

    def append_end(self, value):
        node = Node(value)
        if self.root.next == None:
            self.root.next = node
        else:
            self.end.next = node
            node.top = self.end
        self.end = node

    def append_first(self, value):
        node = Node(value)
        tem_node = self.root.next
        self.root.next = node
        node.next = tem_node
        tem_node.top = node
        self.length += 1

    def remove_first(self):
        tem_node = self.root.next
        self.root.next = tem_node.next
        tem_node.top = self.root
        del tem_node

    def remove_value(self, value):
        for node in self.__iter__():
            tem_node = node.next
            if tem_node.value == value:
                node.next = tem_node.next
                tem_node.next.top = node
                del tem_node
                break

    def remove_end(self):
        for node in self.__iter__():
            if node.next == self.end:
                node.top = self.end.top
                self.end = node
                del node.next
                break


if __name__ == '__main__':
    link = LinkList()
    link.append_end('金吒')
    link.append_end('木吒')
    link.append_end('哪吒')
    for node in link:
        print(node.value)
    print('-' * 10)
    link.append_first('李婧')
    for node in link:
        print(node.value)
    print('-' * 10)
    link.remove_first()
    for node in link:
        print(node.value)
    print('-' * 10)
    link.remove_value('木吒')
    for node in link:
        print(node.value)
    print('-' * 10)
    link.remove_end()
    for node in link:
        print(node.value)
