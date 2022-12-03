def moveZeroes(nums):
    zeroes = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            zeroes += 1
            nums.pop(i)
            continue
        i += 1

    nums.extend([0 for _ in range(zeroes)])

a = [0, 0, 1, 2, 5, 0, 3, 10]
b = [0, 0, 1]
c = [0,0,0,0,0,0,1,1,1]
moveZeroes(a)
moveZeroes(b)
moveZeroes(c)

print(a)
print(b)
print(c)
