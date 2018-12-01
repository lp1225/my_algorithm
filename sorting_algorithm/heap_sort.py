# 堆排序 先求大根堆，然后子节点与父节点比较，排序

# def swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp

# def heapSort(arr):
#     """求大根堆
#        再排序
#     """
#     if arr == None or len(arr)<2:
#         return 
#     i = len(arr)-1
#     # 得到第一个大根堆
#     while i >= 0:
#         heapinsert(arr, i)
#         i -= 1 
#     heapfiy(arr,len(arr)-1)
#     return arr

# def heapfiy(arr, end):
#     """每次都去得到大根堆"""
#     while end >=0:
#         if arr[0] > end:
#             swap(arr, 0 ,end)
#             end -= 1
#             i = 0
#             while i <= end:
#                 heapinsert(arr, i)
#                 i += 1
    
# def heapinsert(arr, index):
#     """如果子节点比父节点大，change"""
#     while arr[index] > arr[int((index-1)/2)]:
#         swap(arr, index, int((index-1)/2) )
#         index = int((index-1)/2)
#     return arr


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def heapSort(arr):
    """"堆排序，无bug版"""
    # 先求大根堆
    if arr == None or len(arr) < 2:
        return
    i = 0
    while i <= len(arr)-1:
        heapInsert(arr, i)
        i += 1
    size = len(arr)
    size = size-1
    swap(arr, 0, size)
    while size > 0:
        heapify(arr, 0, size)
        size -= 1
        swap(arr, 0, size)
        # size -= 1
    return arr


def heapInsert(arr, index):
    """"判断子节点和父节点的大小"""
    while arr[int((index - 1)/2)] < arr[index]:
        swap(arr, index, int((index - 1)/2))
        index = int((index - 1)/2)


def heapify(arr, index, size):
    """"维护这个堆为大根堆"""
    left = 2*index+1
    while left < size: # 越界条件
        # 同级比较
        largest = left+1 if left+1 < size and arr[left+1] > arr[left] else left
        # 与父级比较
        largest = largest if arr[largest] > arr[index] else index

        if largest == index:
            break
        swap(arr, index, largest)
        index = largest
        left = 2*index+1

arr = [7, 5, 6, 4, 9, 8]
a = heapSort(arr)
print(a)
print('-----------------------------------------')
# arr2 = []
# import random
# for i in range(100):
#     arr2.append(random.randint(0, 1000))
# result = heapSort(arr2)
# print(result)
arr = [1, 5, 5, 5, 6]
a = heapSort(arr)
print(a)
print('-----------------------------------------')
arr = [1, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 5, 6, 6, 7]
a = heapSort(arr)
print(a)
