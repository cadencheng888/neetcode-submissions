from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = defaultdict(int)
        s1_set = set(s1)
        l = 0
        s2_map = defaultdict(int)
        for i in range(len(s1)):
            s1_map[s1[i]] += 1
        for r in range(len(s2)):
            rightChar = s2[r]
            s2_map[rightChar] += 1
            if r - l + 1 > len(s1):
                leftChar = s2[l]
                s2_map[leftChar] -= 1
                if s2_map[leftChar] == 0:
                    del s2_map[leftChar]
                l += 1
            if s2_map == s1_map:
                return True
        return False   
            
        