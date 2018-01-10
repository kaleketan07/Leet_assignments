def isHappy(n):
    sum = 0
    sumarr = []
    if n == 1:
        return True
    else:
        while 1:
            while n > 0:
                ## add digits' square
                rem = n % 10
                print "rem :" , rem
                n = n / 10
                print "n:", n
                sum += rem ** 2
                print "sum:", sum
            if sum == 1:
                return True
            elif sum in sumarr:
                return False
            else:
                n = sum
                sumarr.append(sum)
                sum = 0
if __name__ == '__main__':
    print isHappy(234)
