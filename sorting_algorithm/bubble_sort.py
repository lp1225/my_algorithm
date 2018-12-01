# 排序[2, 6, 9, 4, 8, 7]

def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp

def Bubble_sort(arr):
    if len(arr) < 2:
        return 
    end = len(arr)-1
    flag = 0
    while end > 0:
        flag += 1
        for i in range(end):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
        end -= 1
    return arr, flag

def Bubble_sort02(arr):
    """优化,定义一个标记判断什么时候数组有序"""
    end = len(arr)-1
    flag = 0
    while end > 0:
        sum = 0
        flag += 1
        for i in range(end):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                sum += 1
        if sum == 0:
            print('剩余的数是已排好的')
            break
        end -= 1
    return arr, flag

def Bubble_sort03(arr):
    """ 前半部分（3，4，2，1）无序，后半部分（5，6，7，8)
        比较后确定最后无序区边界,
        边界问题
    """
    end = len(arr)-1
    flag = 0
    lastexchangeindex = 0  # 最后无序区的边界
    while end >= 0:
        flag += 1
        change = False
        for i in range(end):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                change = True
                lastexchangeindex = i+1         
        sortBorder = lastexchangeindex
        print(end)
        if change == True:
            print('你已找到最后无序区边界', sortBorder)
            end = sortBorder
        end -=1
    return arr, flag

print("------------------------")
arr_test = [2, 6, 9, 4, 8, 7]
result = Bubble_sort(arr_test)
print(result)

print('------------------------')
arr_test = [2, 6, 9, 4, 8, 7]
result = Bubble_sort02(arr_test)
print(result)

print('------------------------')
arr_test = [3, 4, 2, 1, 5, 6, 7, 8]
result = Bubble_sort03(arr_test)
print(result)
