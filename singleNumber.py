
def singleNumber(nums):
    for i in range(1,len(nums),1):
        nums[0] ^= nums[i]
    print nums[0]


if __name__ == '__main__':
    singleNumber([2,2,3,3,5])
