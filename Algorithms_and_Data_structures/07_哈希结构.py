class Array:
    def __init__(self, size=4):
        self.__size = size
        self.__items = [None] * size
        self.length = 0

    def __setitem__(self, index, value):
        self.__items[index] = value
        self.length += 1
        if self.enough():
            self.kuo_rong()

    def __getitem__(self, index):
        return self.__items[index]

    def __len__(self):
        return self.__size

    def __iter__(self):
        for i in range(self.__size):
            yield self.__items[i]

    def clear(self):
        for i in range(self.__size):
            self.__items[i] = None

    def find_value(self, value):
        index = -1
        for i, v in enumerate(self.__items):
            if v == value:
                index = i
                break
        return index

    '吕布  貂蝉  董卓  张辽'
    '0      1     2    3'

    def remove(self, value):
        index = self.find_value(value)
        if index != -1:
            for i in range(index, self.__size):
                if i == self.__size - 1:
                    self.__items[i] = None
                    break
                self.__items[i] = self.__items[i + 1]
            self.length -= 1
        else:
            return '没有此值'

    def add_first(self, value):
        # if self.length >= self.__size:
        #     return '满了'
        # else:
        for i in range(self.length, -1, -1):
            self.__items[i] = self.__items[i - 1]
        self.__items[0] = value
        if self.enough():
            self.kuo_rong()

    def kuo_rong(self):
        old = self.__items
        self.__size = self.__size << 1
        self.__items = [None] * (self.__size)

        for i in range(len(old)):
            self.__items[i] = old[i]

    def enough(self):
        return self.length / float(self.__size) > 0.8


class Slot:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return 'key:{}  value:{}'.format(self.key, self.value)


class HashTable:
    def __init__(self):
        self.size = 4
        self.items = Array(self.size)

    def get_index(self, key):
        return hash(key) % self.size

    def find_index_to_insert(self, key):
        index = self.get_index(key)
        # index索引所在的位置上的值是None
        if self.items[index] == None:
            return index
        else:
            # index索引所在的位置上的有值
            while self.items[index] is not None:
                # key 就是我们要插入的key
                if self.items[index].key == key:
                    return index
                else:
                    # key 不是我们要插入的key
                    index = (5 * index + 1) % self.size
            return index

    def put(self, key, value):
        slot = Slot(key, value)
        index = self.find_index_to_insert(key)
        self.items[index] = slot

    def find_key(self, key):
        index = self.get_index(key)
        # index索引所在的位置上的值是None
        if self.items[index] == None:
            return None
        else:
            # index索引所在的位置上的有值
            while self.items[index] is not None:
                # key 就是我们要插入的key
                if self.items[index].key == key:
                    return index
                else:
                    # key 不是我们要插入的key
                    index = (5 * index + 1) % self.size
            return None

    def get(self, key):
        index = self.find_key(key)
        if index is not None:
            return self.items[index]
        else:
            return '没有此Key'

    def __iter__(self):
        for s in self.items:
            if s is not None:
                yield s.key


if __name__ == '__main__':
    hash_table = HashTable()
    # print(hash_table.get_index('ab'))
    hash_table.put('name', '曹操')
    hash_table.put('age', '40')
    hash_table.put('age2', '50')
    # print(hash_table.get('name'))
    print(hash_table.get('age2'))
    print(hash_table.get('sex'))
    # for h in hash_table:
    #     print(h)
