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

def findMaxConsecutiveOnes(nums):
    a = []
    b = 0
    for i in nums:
        if i != 0:
            b += 1
        else:
            a.append(b)
            b = 0
    a.append(b)
    return max(a)

findMaxConsecutiveOnes([1])

a = [1, 2, 3, 4,]
print(a.index(2))
