def twoSum(numbers, target):
    if target > 0:
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] <= target:
                last_i = i
                break

        for i in range(last_i, -1, -1):
            for j in range(i - 1, -1, -1):
                if numbers[i] + numbers[j] == target:
                    return [j + 1, i + 1]

    elif target < 0:
        for i in range(0, len(numbers)):
            if numbers[i] >= target:
                first_i = i
                break

        for i in range(first_i, len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

    else:
        for i in range(0, len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

l = [1, 3, 4, 6, 10]
print(twoSum(l, 11))
