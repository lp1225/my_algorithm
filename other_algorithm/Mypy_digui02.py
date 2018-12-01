# 冒泡递归  2, 6, 9, 4, 8, 7


def bubble(arr, l, r):
    """冒泡递归"""
    if l == r:
        return
    end = len(arr)-1
    for i in range(end):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
    bubble(arr, l, r-1)
    return arr


if __name__ == '__main__':
    arr_test = [2, 6, 9, 4, 8, 7]
    result = bubble(arr_test, 0, len(arr_test)-1)
    print(result)
