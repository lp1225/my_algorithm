# [2, 6, 9, 4, 8, 7] 通过步速对插入排序优化


def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        # 进行插入排序
        for i in range(gap, n):
            key = arr[i]
            j = i-gap
            while arr[j] > key and j >= 0:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = key
        gap //=2
    return arr


arr_test = [2, 2, 6, 9, 4, 8, 7]
result = shellSort(arr_test)
print(result)
