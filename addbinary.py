def addBinary(a, b):
    sum = ""
    carry = "0"
    zeroes = ""
    if len(a) > len(b):
        temp = b
        for i in range(0, len(a)-len(b), 1):
            zeroes = zeroes +'0'
        b = zeroes + temp

    if len(b) > len(a):
        temp = a
        for i in range(0, len(b)-len(a), 1):
            zeroes = zeroes +'0'
        a = zeroes + temp

    for i in range(len(a)-1, -1, -1):
        if a[i] == "1" and b[i] == "1" and carry == "0":
            sum = "0" + sum
            carry = "1"
        elif a[i] == "1" and b[i] == "1" and carry == "1":
            sum = "1" + sum
            carry = "1"
        elif a[i] == "1" and b[i] == "0" and carry == "0":
            sum = "1" + sum
            carry = "0"
        elif a[i] == "1" and b[i] == "0" and carry == "1":
            sum = "0" + sum
            carry = "1"
        elif a[i] == "0" and b[i] == "1" and carry == "0":
            sum = "1" + sum
            carry = "0"
        elif a[i] == "0" and b[i] == "1" and carry == "1":
            sum = "0" + sum
            carry = "1"
        elif a[i] == "0" and b[i] == "0" and carry == "0":
            sum = "0" + sum
            carry = "0"
        elif a[i] == "0" and b[i] == "0" and carry == "1":
            sum = "1" + sum
            carry = "0"
        else:
            sum = ""
    if carry == "1":
        print carry + sum
    else:
        print sum
if __name__ == '__main__':
    addBinary("10", "10")



        #
