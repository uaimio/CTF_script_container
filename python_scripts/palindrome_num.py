class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) / 2):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return False
        
        return True