from copy import deepcopy

'''插入排序：每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
    时间复杂度：O(n^2)'''


def insert_sort(array):
    op = deepcopy(array)
    for i in range(1, len(op)):
        for j in range(i, 0, -1):
            if op[j] < op[j - 1]:
                op[j], op[j - 1] = op[j - 1], op[j]  # 注意此时j-1>j
    return op


if __name__ == '__main__':
    num = [1, 2, 3, 5, 1, 68, 23, 8, 51, 3, 8]
    print(num)
    print('----- 排序后 ------')
    print(insert_sort(num))
