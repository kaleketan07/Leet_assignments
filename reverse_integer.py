def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    temp = x
    res = 0
    num = 0
    while abs(x) != 0:
        res = abs(x) % 10
        num += res * pow(10, len(str(abs(x))) - 1)
        print "num : ", num
        x = abs(x) / 10
        print "x : ", x
    if temp > 0 and temp < (pow(2,31)-1):
        return num
    elif temp < 0 and temp >(-(pow(2,31))):
        return -num
    else: return 0