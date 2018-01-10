def oneStr(s):
    print type(s)
    print s
    stack = []
    res = ""
    for i in range(len(s)):
        if i == 0:
            curr = s[i]
            stack.append(s[i])
        else:
            if s[i] == curr:
                stack.append(s[i])
            else:
                curr = s[i]
                res = res + str(len(stack)) + str(stack.pop())
                stack = []
                stack.append(s[i])

    return res + str(len(stack)) + str(stack.pop())

def countAndSay(n):
    if n == 1:
        return "1"
    elif n == 2:
        return oneStr("1")
    else:
        return oneStr(countAndSay(n-1))

if __name__ == '__main__':

    countAndSay(7)

