class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        result = []
        current = []

        def backtrack(start):
            if start == len(s):
                result.append(current.copy())
                return
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    current.append(s[start:i + 1])
                    backtrack(i + 1)
                    current.pop()
        backtrack(0)
        return result