
'''
归并排序： 分为两部分，先拆分，在合并，利用递归，把目标数组，数次平分直到长度为1 ，载每个相邻的两组进行对比，并且合并，最终完成排序
时间复杂度为：O(n log n)

'''
def merge(a, b):
    '''合并操作'''
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    '''拆分'''
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2  # 规定分成子序列的长度
    left = merge_sort(lists[:middle])  # 把左边的再次拆分
    right = merge_sort(lists[middle:])  # 右边的再拆分
    return merge(left, right)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(merge_sort(a))
