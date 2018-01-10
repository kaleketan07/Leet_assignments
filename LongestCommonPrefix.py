## Given an array of strings find the longest common prefix in all of those strings

#strs = ["Mr. Ketan", "Mr. Anish12", "Mr. Sachin", "Mr. Akhil123", "Mr. Aditya1234"]
strs = ["aa", "aa"]
## find the string with min length
i = 0
if len(strs) > 1:
    min_str =  min(strs, key= lambda str: len(str))
    if len(min_str)<=1:
        if all(strs[j].startswith(min_str) for j in range(0, len(strs), 1)):
            print min_str
        else: print ""

    else:
        for i in range(0, len(min_str),1):
            print "in for: ", i
            if not all(strs[j].startswith(min_str[:i+1])for j in range(0, len(strs), 1)):
                print "i:", i
                return min_str[:i]
            return min_str[:i]

elif len(strs) == 1:
    print strs[0]
else: print ""

# print sorted(arr, key= lambda str: len(str))
