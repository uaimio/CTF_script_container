class Solution:
    def findMaximumXOR(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] ^ nums[1]

        prec_num1 = nums[0]
        prec_num2 = nums[1]
        ret = prec_num1 ^ prec_num2

        for i in range(2, len(nums)):
            xor_num1 = prec_num1 ^ nums[i]
            xor_num2 = prec_num2 ^ nums[i]

            if xor_num1 > ret or xor_num2 > ret:
                if xor_num1 >= xor_num2:
                    ret = xor_num1
                    prec_num2 = nums[i]
                else:
                    ret = xor_num2
                    prec_num1 = nums[i]


        return ret


def main():
    value1 = Solution.findMaximumXOR(None, [3,10,5,25,2,8])
    value2 = Solution.findMaximumXOR(None, [14,70,53,83,49,91,36,80,92,51,66,70])
    value3 = Solution.findMaximumXOR(None, [10,1,3,4,7,15,18,35])
    print(f'Value1={value1}, Value2={value2}, Value3={value3}')

if __name__ == '__main__':
    main()