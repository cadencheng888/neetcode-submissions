from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = defaultdict(list)
        result = []
        for word in strs:
            char_array = [0] * 26
            for char in word:
                char_array[ord(char) - ord('a')] += 1
            words[tuple(char_array)].append(word)
        for values in words.values():
            result.append(values)
        return result
        