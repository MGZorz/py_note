from datetime import datetime

'''二分查找1'''
num = range(1, 10)


def binary_search(array, value):
    begin = 0
    end = len(array) - 1
    while begin < end:  # 开始要小于结束
        mid = (begin + end) // 2  # 求均值
        if value > array[mid]:  # 如果value大于中间值
            begin = mid + 1  # 那么把begin值变为中间值+1，相当于把array舍去mid+ 1之前的部分
        elif value < array[mid]:
            end = mid - 1  # 那么把end值变为中间值-1，相当于把array舍去mid-1之后的部分
        else:
            return mid
    return


'''二分查找2'''


def bin_search(array, value):
    low = 0  # 最小数下标
    high = len(array) - 1  # 最大数下标
    while low <= high:
        mid = (low + high) // 2  # 中间数下标
        if array[mid] == value:  # 如果中间数下标等于val, 返回
            return mid
        elif array[mid] > value:  # 如果val在中间数左边, 移动high下标
            high = mid - 1
        else:  # 如果val在中间数右边, 移动low下标
            low = mid + 1
    return  # val不存在, 返回None


if __name__ == '__main__':
    for i in num:
        print(i)

    print(bin_search(num, 10))
    print(binary_search(num, 10))
