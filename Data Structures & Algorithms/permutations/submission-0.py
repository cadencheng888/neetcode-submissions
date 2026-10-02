class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = [False] * len(nums)
        result = []
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
            for i in range(len(nums)):
                if seen[i] == True:
                    continue
                path.append(nums[i])
                seen[i] = True
                backtrack()
                path.pop()
                seen[i] = False
        backtrack()
        return result
