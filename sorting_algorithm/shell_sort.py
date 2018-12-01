# 希尔排序

def insertSort(arr):
    """进行直接插入排序"""
    i = 1
    end = len(arr)-1

    while i <= end:
        j = i-1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr

def shellSort(list):
    """进行希尔排序"""
    i =0
    j =0
    n = len(list)
    gap =n//2
    while gap >0:
        # 每个步长进行直接插入排序
        for i in range(gap,n):
            # 直接插入排序
            temp = list[i]
            j = i
            while list[j-gap] > temp and j >= gap:
                list[j] = list[j-gap]
                j -= gap
            list[j] = temp
        gap //=2
    return list

if __name__ == '__main__':
    arr_test = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    result = insertSort(arr_test)
    print(result)
    print('-----------------------------------------')
    arr_test = [49, 38, 65, 97, 26, 13, 27, 49, 55, 4]
    result = shellSort(arr_test)
    print(result)
