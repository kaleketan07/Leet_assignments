s = " "

if s == "":
    print 0
else:
    list = s.split()
    if len(list) == 0:
        print 0
    else:
        print len(list[len(list) - 1])