class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        maxLen = 0
        charSet = set()
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            length = right - left + 1
            maxLen = max(maxLen, length)
        
        return maxLen
            