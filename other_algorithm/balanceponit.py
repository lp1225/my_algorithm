# 平衡点问题

def getPoint(arr):
    """get ponit"""
    if len(arr) < 2:
        return
    tag = 1
    help = []
    while tag < len(arr):
        sum = 0
        sum_after = 0
        for i in range(tag):
            sum += arr[i]
        for i in range(tag+1, len(arr)):
            sum_after += arr[i]
        if sum == sum_after:
            help.append(arr[tag])
        tag += 1
    return help

if __name__ == '__main__':
    arr_test = [1,2,5,7,6,8,0,21,0]
    result = getPoint(arr_test)
    print(result)
