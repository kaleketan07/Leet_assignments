def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    temp = ""
    if s == "":
        return True
    else:
        for i in range(len(s)):
            if s[i].isalnum():
                temp = temp + s[i].lower()

    print temp
    j = 0
    k = len(temp)-1
    while i < j:
        if temp [i] != temp [j]:
            return False
    return True


if __name__ == '__main__':
    print isPalindrome("A man, a plan, a canal: Panama")