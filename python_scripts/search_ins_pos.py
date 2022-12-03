def searchInsert(nums, target) -> int:
    t = 0
    while True:
        lm = len(nums)
        if lm == 1:
            return 0 if target <= nums[0] else t + 1

        i = int(lm / 2)
        if target == nums[i]:
            return t + i
        elif target < nums[i] and target > nums[i - 1]:
            return t + i
        elif target < nums[i]:
            nums = nums[:i]
        elif target > nums[i]:
            nums = nums[i:]
            t += i
        else:
            print('Condizione non ammessa')
            raise Exception
        
print(searchInsert([-3, 1, 2, 4], 0))