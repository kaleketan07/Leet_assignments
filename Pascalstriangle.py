
def generate(numRows):
    l =[[1],[1,1]]
    for i in range(1, numRows):
        l.append([1])
        for j in range(len(l[i-1])+1):
            if j == 0:
                l[i][j] = l[i-1][j]
            elif j == len(l[i-1]):
                l[i].append(l[i-1][j-1])
            else:
                l[i].append(l[i-1][j-1]+l[i-1][j])
    print l

if __name__ == '__main__':
    generate(9)
