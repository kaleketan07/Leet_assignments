def removeElement(nums, val):
    begin = 0
    for i in range(0, len(nums), 1):
        if (nums[i]!= val):
            nums[begin] = nums[i]
            begin += 1
    print nums, begin
if __name__ == '__main__':
    removeElement([3, 2, 2, 3, 4, 5, 3], 3)

