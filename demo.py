def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 0:
        return False
    x, i = 0, 1
    while x < num:
        x += i
        i += 2
        print(x, i)

    return x == num


def gcd(a, b):
    if (b == 0):
        return a
    else:
        print(a, b)
        return gcd(b, a % b)


a = 0


def fib(n):
    global a
    a += 1
    if(n == 0):
        return 1
    elif(n == 1):
        return 2
    else:
        return fib(n-1)+fib(n-2)


fib(9)
print(a)
