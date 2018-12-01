# 递归


def sum(arr, n):
    """递归求和"""
    if n == 0:
        return arr[0]
    else:
        return sum(arr, n-1)+arr[n]


def get_max(arr, n):
    """求最大值"""
    if n == 0:
        return arr[0]
    if get_max(arr, n-1) > arr[n]:
        return get_max(arr, n-1)
    else:
        return arr[n]


def find_max(arr, l, r):
    """查找范围内的最大值"""
    if l == r:
        return arr[l]
    else:
        if arr[l] < find_max(arr, l+1, r):
            return find_max(arr, l+1, r)
        else:
            return arr[l]


def find_max02(arr, l, r):
    """二分递归"""
    if l == r:
        return arr[l]
    else:
        mid = int((l+r)/2)
        max_left = find_max02(arr, l, mid)
        max_right = find_max02(arr, mid+1, r)
        return max(max_left, max_right)
    

if __name__ == '__main__':
    arr_test = [9, 1, 4, 2, 8, 6]
    result = sum(arr_test, len(arr_test)-1)
    print(result)
    result = get_max(arr_test, len(arr_test)-1)
    print(result)
    result = find_max(arr_test, 0,len(arr_test)-1)
    print(result)
    result = find_max02(arr_test, 0, len(arr_test)-1)
    print(result)
