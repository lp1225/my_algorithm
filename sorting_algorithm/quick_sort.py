# 快速排序

def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

def quicksort(arr, l, r):
    # 退出条件即为，上一次的小于区的left为本次l的r，单他们重合则必然有序，退出
    # rigth同理
    if l < r:
        p = partition(arr, l, r)
        quicksort(arr, l, p[0]-1)
        quicksort(arr, p[1]+1, r)
    return arr

def partition(arr, l, r):
    """划分"""
    less = l-1
    more = r 
    while l < more:
        if arr[l] < arr[r]:
            less += 1
            swap(arr, less, l)
            l += 1
        elif arr[l] > arr[r]:
            more -= 1
            swap(arr, l, more)
        else:
            l += 1
    swap(arr, more, r)
    arr02 = [less+1, more]
    return arr02

array_test = [2, 6, 9, 4, 6, 8, 7]
result = quicksort(array_test,0, len(array_test)-1)
print(result)
    

