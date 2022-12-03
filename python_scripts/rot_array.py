def rotate(nums, k):
    l = len(nums)
    li = []

    for i in range(l):
        if i + k >= l:
            li.append(nums[i])

    li = li + nums[:l-k]
    from copy import deepcopy
    nums = deepcopy(li)

    print('Just debug')

def rotate1(nums, k):
    l = len(nums)
    k = k % l
    if k == 0:
        return
    
    temp = [0, 0]
    for i in range(k):
        j = 0
        index1 = i
        index2 = (i + k) % l

        for _ in range(int(l/k) + 1):
            temp[j % 2] = nums[index2]
            if j == 0:
                nums[index2] = nums[index1]
            else:
                nums[index2] = temp[(j+1) % 2]
            
            j += 1
            index1 = index2
            index2 = (index1 + k) % l

            #if index1 >= i:
            #    break



l1 = [1,2,3,4]
l2 = [1,2,3,4,5,6,7,8,9]
rotate1(l1, 1)
rotate1(l2, 2)

print(l1, l2)
