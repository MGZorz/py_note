class Node:
    def __init__(self, next=None, value=None):
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

    def add(self, value=None):
        pass
