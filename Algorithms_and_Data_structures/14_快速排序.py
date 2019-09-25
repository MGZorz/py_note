'''
快速排序
'''


def quick_query(array):
    if len(array) >= 2:
        mid = array[len(array) // 2]
        left, right = [], []
        array.remove(mid)
        for i in array:
            if i <= mid:
                left.append(i)
            else:
                right.append(i)
        return quick_query(left) + [mid] + quick_query(right)
    else:
        return array


if __name__ == '__main__':
    num = [1, 2, 6, 8, 13, 5, 87, 5, 1]
    print(quick_query(num))
