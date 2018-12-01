# 选择排序

def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

def selectSort(arr):
    """选择排序"""
    end = len(arr)-1
    minindex = 0
    while end >0:
        for i in range(minindex, len(arr)):
            if arr[minindex] > arr[i]:
                swap(arr, i , minindex)     
        minindex += 1
        end -= 1
    return arr

array_test = [2, 6, 9, 4, 8, 7]
result = selectSort(array_test)
print(result)
