def maxSubarray(nums):
    sum = nums[0]
    maxSum = nums[0]
    i = 1
    if len(nums) == 1:
        return nums[0]
    else:
        while i < (len(nums)):
            sum = max(sum + nums[i], nums[i])
            print "sum when i =", i, sum
            maxSum = sum if sum > maxSum else maxSum
            print "maxsum when i =", i,maxSum
            i+=1
        return maxSum


if __name__ == '__main__':
   print maxSubarray([-2,-1])



