def getSum(a,b):

    if a > 0 and b > 0:
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return b
    elif a > 0 and b < 0:
        if abs(b) > abs(a):



if __name__ == '__main__':
    print getSum(-2, -7)
