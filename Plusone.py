
def plusOne(digits):
    carry = 0
    new = []
    for i in range(len(digits) - 1, -1, -1):
        if len(digits) == 1:
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
                new.append(carry)
                for j in range(1, len(digits) + 1):
                    new.append(digits[j-1])
                return new
            else:
                digits[i] = 1 + digits[i]
        elif i == 0:
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
                new.append(carry)
                for j in range(1, len(digits) + 1):
                    new.append(digits[j-1])
                return new
            else:
                digits[i] = carry + digits[i]

        elif i == len(digits) - 1:
            if digits[i] == 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = 1 + digits[i]

        else :
            if digits[i] + carry == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = digits[i] + carry

    return digits

if __name__ == '__main__':
   print plusOne([0])


