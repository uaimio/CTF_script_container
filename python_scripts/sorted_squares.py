def sortedSquares(nums):
    l = list()

    i_min = 0

    for i in range(len(nums)):
        square = nums[i] ** 2
        if i == 0:
            l.append(square)
        elif square >= l[i - 1]:
            l.append(square)
        elif square <= l[0]:
            l = [square] + l
        elif square >= l[i - 2]:
            l = l[:i-1] + [square] + l[i-1:]
        else:
            print('Condizione non ammessa')
            raise Exception

    return l

def sortedSquares1(nums):
    lun = len(nums)
    if lun == 1:
        return [nums[0] ** 2]
    
    l = list()
    i = 0
    j = lun - 1

    #if lambda x, y: x ^ y 
    while True:
        if nums[i] >= 0 and nums[j] <= 0:
            break
        elif nums[j] < 0:
            pass

        elif nums[i] < 0 and nums[j] > 0:
            l = [nums[i] ** 2, nums[j] ** 2] + l
            i += 1
            j -= 1

    while i != j:
        l = [0, 0] + l
        i += 1
        j -= 1

    if i == j:
        l = [nums[i] ** 2] + l

    return l

def sortedSquares2(nums):
    if len(nums) == 1:
        return [nums[0] ** 2]

    i = 0
    l1 = list()
    l2 = list()
    
    while i < len(nums) and nums[i] < 0:
        l1 = [nums[i] ** 2] + l1
        #l1.append(nums[i] ** 2)
        i += 1

    while i < len(nums):
        l2.append(nums[i] ** 2)
        i += 1

    i = 0
    j = 0
    l_ret = list()
    
    for _ in range(len(nums)):
        if i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                l_ret.append(l1[i])
                i += 1
            elif l2[j] < l1[i]:
                l_ret.append(l2[j])
                j += 1
        elif i < len(l1):
            l_ret.append(l1[i])
            i += 1
        elif j < len(l2):
            l_ret.append(l2[j])
            j += 1
        else:
            print('Condizione non ammessa')
            raise Exception

    return l_ret

print(sortedSquares([-3, 0, 1, 2, 7]))
a = [-10000,-9999,-7,-5,0,0,10000]
b = [-5,-4,1,2,5]
print(sortedSquares2(a))
print(sortedSquares2(b))

#print(sortedSquares1([-3, 0, 1, 2, 7]))
