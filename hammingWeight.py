def hammingWeight(n):
    i = 0
    count = 0
    while i < 32:
        if n & (1 << i):
            count += 1
            i += 1
        else:
            i += 1

    return count


if __name__ == '__main__':
    print hammingWeight(11)