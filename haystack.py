def strStr(haystack,needle):

    if len(needle) == 0:
        return 0
    elif (len(haystack) == 0 and len(needle)!=0) or len(haystack) < len(needle):
        return -1
    else:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if len(needle) == 1:
                    return i
                if len(haystack) - i < len(needle):
                    return -1
                else:
                    for j in range(1, len(needle)):
                        if i+j < len(haystack) and j == len(needle) - 1 and haystack[i+j] == needle[j]:
                             print "here"
                             return i;

                        if i+j < len(haystack) and haystack[i+j] == needle[j]:
                            print "comparing: ", haystack[i+j] , needle[j]
                            continue
                        else:
                            if i < len(haystack) - 1:
                                break
                            else:
                                return -1
            else:
                print haystack[i]
                continue
        return -1

if __name__ == '__main__':

 print strStr("aaa", "aaa")


