# 暴力匹配算法

def violentMatch(s, p):
    """暴力匹配"""
    slen = len(s)
    plen = len(p)
    i = 0
    j = 0
    while i < slen and j < plen:
        if s[i] == p[j]:
            # 匹配成功
            i += 1
            j += 1
        else:
            # 匹配失败，回溯
            i = i-j+1
            j = 0
    
    # 成功返回p在s中的位置，否则返回 -1
    if j == plen:
        return i-j
    else:
        return -1

if __name__ == '__main__':
    s = 'BBC ABCDAB ABCDABCDABDE'
    p = 'ABCDABD'
    result = violentMatch(s, p)
    print(result) 
