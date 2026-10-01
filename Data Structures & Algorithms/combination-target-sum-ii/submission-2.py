class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(start, cur, total):

            if total == target:
                result.append(cur.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                cur.append(candidates[i])
                backtrack(i + 1, cur, total + candidates[i])
                cur.pop()
        backtrack(0, [], 0)
        return result