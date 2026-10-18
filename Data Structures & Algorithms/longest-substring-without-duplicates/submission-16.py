class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        length = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                length -= 1
            char_set.add(s[r])
            length += 1
            maxLen = max(length, maxLen)
        return maxLen