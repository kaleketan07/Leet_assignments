def reverseBits(n):
    print bin(n)
    return int((bin(n)[2:]).zfill(32)[::-1],2)

if __name__ == '__main__':
    print reverseBits(43261596)
