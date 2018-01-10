def isValid(s):
    stack = []

    for i in range(0, len(s)):
        print "s:", s, "length: ", len(s)
        if s[i] == "{" or s[i] == "(" or s[i] == "[":
            print "added:", s[i]
            stack.append(s[i])
        elif s[i] == "}":
            print "here "
            if len(stack) == 0 or i == 0:
                return False
            else:
                if stack.pop() == "{":
                    continue
                else:
                    return False

        elif s[i] == ")":
            if len(stack) == 0 or i == 0:
                return False
            else:
                if stack.pop() == "(":
                    continue
                else:
                    return False
        elif s[i] == "]":
            if len(stack) == 0 or i == 0:
                return False
            else:
                if stack.pop() == "[":
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True
    else: return False

if __name__ == '__main__':
    print isValid("({})")