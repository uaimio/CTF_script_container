def search(nums, target) -> int:
    t = 0
    while True:
        l = len(nums)
        if l == 1 and target != nums[0]:
            return -1
        elif l == 1 and target == nums[0]:
            return t

        i = int(l / 2)
        if target == nums[i]:
            return t + i
        elif target < nums[i]:
            nums = nums[:i]
        elif target > nums[i]:
            nums = nums[i:]
            t += i
        else:
            print('Condizione non ammessa')
            raise Exception


print(search([-3, 1, 2, 4], 0))
