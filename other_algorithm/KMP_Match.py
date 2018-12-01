# Kmp算法匹配字符串

def kmpSearch(s, p):
    """kmp匹配"""
    i = 0
    j = 0
    slen = len(s)
    plen = len(p)
    next = getNext(p)
    while i < slen and j < plen:
        # 如果j == -1或者当前字符匹配成功即 s[i] == p[j]
        # i++, j++
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == plen:
        return i-j
    else:
        return -1

def getNext(p):
    """递推求next数组"""
    next = [None]*len(p)
    next[0] = -1
    plen = len(p)
    k = -1
    j = 0
    while j < plen-1:
        #p[k]表示前缀，p[j]表示后缀
        if k == -1 or p[j] == p[k]:
            k += 1
            j += 1
            # 比较之前next数组求法
            if p[j] != p[k]:
                next[j] = k
            else:
                # 因为不能出现p[j] = p[ next[j ]]，所以当出现时需要继续递归
                # ，k = next[k] = next[next[k]]
                next[j] = next[k]
        else:
            k = next[k]
    print(next)
    return next

# # p = 'ABCDABD'
# p = 'abcabc'
# getNext(p)
if __name__ == '__main__':
    s = 'abcabc'
    p = 'cab'
    result = kmpSearch(s, p)
    print(result)

