# 归并排序 [2, 6, 9, 4, 8, 7]

def sortprocess(arr, l, r):
    if l == r:
        return 
    mid = int((l+r)/2)
    sortprocess(arr, l, mid)
    sortprocess(arr, mid+1, r)
    #外排
    merge(arr, l, mid, r)
    return arr

def merge(arr, l, m, r):
    """用到帮助数组，定义p1, p2两指针"""
    help = []
    p1 = l
    p2 = m+1
    # 比较大小
    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    # 越界情况考虑
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    while p1 <= m:
        help.append(arr[p1])
        p1 += 1
    # 复制回原数组
    j = 0
    for i in help:
        arr[l+j] = i
        j += 1

array_test = [2, 6, 9, 4, 8, 7, 4]
result = sortprocess(array_test, 0, len(array_test)-1)
print(result)
