from copy import deepcopy

'''
冒泡排序： 从前到后依次和自己的下一个进行比较，如果下一个比本身小，则交换值
时间复杂度为：O(n)
'''


def Bubbing(num):
    op = deepcopy(num)
    for i in range(len(op) - 1):
        for j in range(len(op) - i - 1):
            if op[j + 1] < op[j]:
                op[j], op[j + 1] = op[j + 1], op[j]
    return op


if __name__ == '__main__':
    # num = [2, 6, 8, 1, 3312, 5, 81, 3, 4, 2]
    num = [1, 2, 3, 4, 5, 6, 0, 9]
    # Bubbing(num)
    print(Bubbing(num))
    print(num)
