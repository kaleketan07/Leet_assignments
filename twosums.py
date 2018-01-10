nums = [2, 3, 4, 1, 7]
target = 8
i = 0
j = 0
while i < len(nums):
    j = i + 1

        while j < len(nums):
            if target - nums[i] == nums[j]:
                print ( i, j)
                break
            else:
                j+=1

        i+=1