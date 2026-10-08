class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []

        def backtrack(start):
            results.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return results
        