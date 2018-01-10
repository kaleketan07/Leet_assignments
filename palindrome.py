def isPalindrome(x):
    if (abs(x) == -int(str(x)[::-1]) if (x<0) else int(str(x)[::-1])) and x in range(-(pow(2,31), pow(2,31)-1)):
        return True
    else:
        return False

if __name__ == '__main__':
    isPalindrome()