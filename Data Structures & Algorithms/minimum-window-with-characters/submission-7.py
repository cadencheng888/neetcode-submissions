class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        result = ""
        minLen = float('inf')
        t_arr = [0] * 128
        for char in t:
            t_arr[ord(char)] += 1
        need = 0
        for count in t_arr:
            if count > 0:
                need += 1
        l = 0
        best_start = 0
        matches = 0
        s_arr = [0] * 128
        for r in range(len(s)):

            char_r = ord(s[r])
            s_arr[char_r] += 1
            if s_arr[char_r] == t_arr[char_r] and t_arr[char_r] > 0:
                matches += 1
                
            while matches == need:
                
                length = r - l + 1
                
                if length < minLen:
                    best_start = l
                    minLen = length
                char_l = ord(s[l])
                s_arr[char_l] -= 1
                if t_arr[char_l] > 0 and s_arr[char_l] < t_arr[char_l]:
                    matches -= 1
                l += 1
        if minLen != float('inf'):
            result = s[best_start:best_start + minLen]
            return result
        return result
                
                
