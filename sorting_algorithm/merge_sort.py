# 归并排序

def mergeSort(arr, l, r):
    """归并排序"""
    if l == r:
        return 
    mid = int((l+r)/2)
    # mid = l + ((r - l) >> 1)
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)
    return arr

def merge(arr, l, mid, r):
    """归并外排"""
    help = []
    p1 =l
    p2 = mid+1
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 +=1
        else:
            help.append(arr[p2])
            p2 +=1
    # 边界划分
    while p1 <= mid:
        help.append(arr[p1])
        p1 +=1
    while p2 <= r:
        help.append(arr[p2])
        p2 +=1
    # 复制回去
    j = 0
    for i in help:
        arr[l+j] = i
        j +=1

array_test = [2, 6, 9, 4, 8, 7]
result = mergeSort(array_test, 0, len(array_test)-1)
print(result)
print('---------------------')
import random
array_02 = [random.randint(0,100) for i in range(100)]
result02 = mergeSort(array_02, 0, len(array_02)-1)
print(result02)
