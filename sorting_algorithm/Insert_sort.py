# 插入排序 [2, 6, 9, 4, 8, 7] 小到大

def insert_sort(arr):
    i = 1
    end =len(arr)-1

    while i <= end:
        j = i-1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1 
        arr[j+1] = key
        i += 1
    return arr

array_test = [5,2, 6, 9, 4, 8, 7]
result = insert_sort(array_test)
print(result)
