def removeDuplicates(nums):
    temp =
    count = 0
    for i in range(len(nums)):
        if nums[i] != temp:
            count += 1
            temp = nums[i]
            nums[count-1] = nums[i]
    print nums

    return count



if __name__ == '__main__':
    print removeDuplicates([1,1,1,2,3,4,5,6,6])
