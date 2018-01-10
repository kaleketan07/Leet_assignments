### Incomplete solution


def maxProduct(nums):
    sum = nums[0]
    brute = nums[0]
    maxSum = nums[0]
    i = 1
    if len(nums) == 1:
        return nums[0]
    else:
        while i < (len(nums)):
            sum = max(sum * nums[i], nums[i])
            brute = brute * nums[i]
            maxSum = sum if sum > brute else brute
            i+=1
        return maxSum


if __name__ == '__main__':
   print maxProduct([-2,3,-2,-4])