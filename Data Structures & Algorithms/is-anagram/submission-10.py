class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for char in s:
            if char not in countS:
                countS[char] = 0
            else:
                countS[char] = countS[char] + 1
        for char in t:
            if char not in countT:
                countT[char] = 0
            else:
                countT[char] = countT[char] + 1
        for char in countS:
            if char not in countT:
                return False
            if countS[char] != countT[char]:
                return False
        return True
        
                      
