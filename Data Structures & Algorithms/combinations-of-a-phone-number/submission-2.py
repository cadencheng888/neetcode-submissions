class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {2: "abc", 3: "def", 4 : "ghi", 5:"jkl", 6:"mno", 
        7:"pqrs", 8:"tuv", 9:"wxyz"}

        path = []
        result = []

        def backtrack(index):
            if len(path) == len(digits):
                result.append("".join(path))
                return
            for char in phone[int(digits[index])]:
                path.append(char)
                print(path)
                backtrack(index + 1)
                path.pop()
        backtrack(0)
        return result