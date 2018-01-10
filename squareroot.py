def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    lo = 1
    hi = x

    while (hi - lo > 1):
        mid = (hi + lo) / 2
        if mid * mid > x:
            hi = mid
        else:
            lo = mid

    return lo

if __name__ == '__main__':
    print mySqrt()


