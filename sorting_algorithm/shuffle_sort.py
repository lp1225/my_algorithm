# 洗牌算法
import random

def myShuffle(arr):
    help = []
    length = len(arr)-1
    while length >= 0:
        index = random.randint(0,length)
        help.append(arr[index])
        arr.pop(index)
        length -= 1
    return help

if __name__ == '__main__':
    test_arr = [1, 8, 9, 6, 7, 6]
    new_arr = myShuffle(test_arr)
    print(new_arr)
