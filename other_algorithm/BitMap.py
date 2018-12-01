# 对于大数据存储的用法

def bit_map(arr):
    print(arr)
    s = 0
    for i in arr:
        # 把1左移i位的值等于2的i次方
        # 之后把该值与s并上等于把该值上所有的1都插入s的对应位置上
        s = s | 1 << i
    # s_list = [i for i in list(str(s)).reverse()]
    s = bin(int(str(s), 10))
    s_str = str(s)[2:]
    s_list = list(s_str)
    s_list.reverse()
    s = ''.join(s_list)
    print(s)


arr = [0, 1, 3, 4, 5, 8, 12, 13, 15, 18, 19, 20, 22, 23, 24]
bit_map(arr)

    
