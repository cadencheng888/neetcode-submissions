import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = collections.defaultdict(int)
        t_chars = collections.defaultdict(int)
        if len(s) != len(t):
            return False
        return collections.Counter(s) == collections.Counter(t)
        for char in s:
            s_chars[char] += 1
        for char in t:
            t_chars[char] += 1
        return s_chars == t_chars
        