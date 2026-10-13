class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digits_map = {
            2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
            5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 
            8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]
        }
        chars = []
        for digit in digits:
            char_num = int(digit)
            chars.append(digits_map[char_num])

        result = []
        path = []

        def backtrack(index):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            for letter in chars[index]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result
