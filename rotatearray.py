def rotate(nums, k):
    k %= len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


    return nums

def reverse(nums, a, b):
    while a < b:
        nums[a], nums[b] = nums[b], nums[a]
        a+=1
        b-=1


if __name__ == '__main__':

    print rotate([1,2], 1)

