from copy import deepcopy

'''
选择排序：第一次先从数组中选出最小的(或者最大的)放在第一位，然后从剩下的未排序的元素中找出最小（最大的）放在第二位，just like
时间复杂度：O(n^2）和插入排序同纬度
'''


def seclection_sort(array):
    for i in range(0, len(array) - 1):  # 遍历索引，0~len（array）-1
        min_ = i  # 设定最小值为min_
        for j in range(i + 1, len(array)):  # 遍历i后的数据
            if array[j] < array[min_]:
                min_ = j
        array[i], array[min_] = array[min_], array[i]


if __name__ == '__main__':
    num = [1, 2, 3, 81, 2, 21, 6, 85, 1, 2, 61, 31]
    print(num)
    seclection_sort(num)
    print(num)
