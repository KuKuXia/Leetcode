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


print(gcd(30, 35))
