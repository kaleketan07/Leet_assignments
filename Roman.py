## Program for Roman number to Integers


## I = 1
## V = 5
## X = 10
## L = 50
## C = 100
## D = 500
## M = 1000

s =  "MCMXCVIII"
num = 0
values = {'I' : 1,
          'V' : 5,
          'X' : 10,
          'L' : 50,
          'C' : 100,
          'D' : 500,
          'M' : 1000}
for i in range(len(s)-1, -1, -1):
    print "i: ", i
    if i == len(s)-1:
        num = num + values[s[i]]
        print "1:",i ,num, values[s[i]]
    elif values[s[i]] < values[s[i+1]]:
        num = num - values[s[i]]
        print "2:",i , num, values[s[i]]
    elif values[s[i]] >= values[s[i+1]]:
        num = num + values[s[i]]
        print "3",i , num, values[s[i]]
print num


