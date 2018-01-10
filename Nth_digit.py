"""class Solution(object):
    digits = {}"""

def findNthDigit(n):
    digits = []
    count =1
    iterator=1
    while iterator <= n+1:
        digits.extend(getdigits(count))
        count+=1
        iterator+=len(getdigits(count))

    return digits[n-2]



"""32 bit di
type n: int
:rtype: int
"""

def getdigits(number):
    digits_in_number = []

    while (number != 0):
        rem = int(number % 10)
        number = int(number / 10)
        digits_in_number.append(rem)
    return digits_in_number[::-1]

def main():
    n= int(input('input: '))
    print('output: ')
    print(findNthDigit(n))

if __name__ == '__main__':
    main()
