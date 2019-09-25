'''线性查找'''
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def line_search(array, value):
    for i, v in enumerate(array):
        if array[i] == value:
            return i


def line_search2(array, value):
    if len(array) == 0:
        return '数组中无任何数据'
    else:
        index = len(array) - 1
        if array[index] == value:
            return index
        else:
            return line_search2(array[:index], value)


if __name__ == '__main__':
    # print(line_search(num, 5))
    print(line_search2(num, 5))
