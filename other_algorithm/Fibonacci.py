# 斐波那契递归， 尾递归

def Fibonacci(n):
    """递归调用"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n-2)+Fibonacci(n-1)

def Fibonacci_tail(n, ret1, ret2):
    """尾递归"""
    if n == 0:
        return ret1
    return Fibonacci_tail(n-1, ret2, ret1+ret2)

result = [Fibonacci(i) for i in range(6)]
print('递归得到的：{}'.format(result))
print('---------------------------------')
result02 = Fibonacci_tail(5, 0, 1)
print(result02)
result02 =[Fibonacci_tail(i, 0, 1) for i in range(5, -1, -1)]
result02.reverse()
print(f'尾递归得到的：{result02}')
