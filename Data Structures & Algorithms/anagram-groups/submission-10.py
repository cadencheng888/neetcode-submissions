from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        str_dict = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for char in string:
                letters[ord(char) - ord('a')] += 1
            str_dict[(tuple(letters))].append(string)
        return list(str_dict.values())

