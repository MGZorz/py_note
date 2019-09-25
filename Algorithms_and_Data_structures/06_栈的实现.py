from collections import deque


class Stack():
    def __init__(self):
        self.item = deque()

    def pop(self):
        return self.item.pop()

    def put(self, value):
        self.item.append(value)


if __name__ == '__main__':
    s = Stack()
    s.put('刘备')
    s.put('关羽')
    s.put('张飞')
    print(s.pop())
    print(s.pop())
    print(s.pop())
