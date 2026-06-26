class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT = {}
        countS = {}
        for char in s:
            if char not in countS:
                countS[char] = 1
            else:
                countS[char] += 1
        for char in t:
            if char not in countT:
                countT[char] = 1
            else:
                countT[char] += 1
        
        for char in s:
            if char not in countT:
                return False
            if countT[char] != countS[char]:
                return False
        return True
                      
