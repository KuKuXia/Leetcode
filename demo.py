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


print(isPerfectSquare(15))
