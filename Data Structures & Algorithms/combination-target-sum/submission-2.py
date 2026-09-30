class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, cur, total):
            if target == total:
                result.append(cur.copy())
                return cur
            if total > target or start >= len(nums):
                return
            cur.append(nums[start])
            backtrack(start, cur, total + nums[start])
            cur.pop()
            backtrack(start+1, cur, total)
        backtrack(0, [], 0)

        return result