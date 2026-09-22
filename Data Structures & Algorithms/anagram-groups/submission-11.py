from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for word in strs:
            char_array = [0] * 26
            for char in word:
                char_array[ord(char) - ord('a')] += 1
            strs_dict[tuple(char_array)].append(word)
        return list(strs_dict.values())