
## Incomplete


def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    else:
        curr = 0
        prev = 0
        for i in range(len(nums)):
            curr, prev = prev, max(curr + nums[i], prev)
            print "curr, prev:" , curr, prev

if __name__ == '__main__':
    rob([7,1,2,8])

