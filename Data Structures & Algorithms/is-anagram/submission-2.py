class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for char in s:
            if char in countS:
                countS[char] = countS[char] + 1
            else:
                countS[char] = 1
        for char in t:
            if char in countT:
                countT[char] = countT[char] + 1
            else:
                countT[char] = 1
        for char in countS:
            if char not in countT:
                return False;
            if countT[char] != countS[char]:
                return False;
        return True
