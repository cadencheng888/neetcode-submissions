class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        right = len(s) - 1
        print(s)
        while left < right:
            print(left, right)
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True