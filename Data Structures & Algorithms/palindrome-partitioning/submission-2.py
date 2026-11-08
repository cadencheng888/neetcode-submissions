class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        start = 0
        def isPalindrome(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def backtrack(start):
            if start == len(s):
                result.append(current.copy())
                return
            for i in range(start, len(s)):
                if isPalindrome(s[start:i + 1]):
                    current.append(s[start:i + 1])
                    backtrack(i + 1)
                    current.pop()
        backtrack(start)
        return result
        