from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            char_arr = [0] * 26
            for char in string:
                char_arr[ord(char) - ord('a')] += 1
            res[tuple(char_arr)].append(string)
        return list(res.values())