from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counts = defaultdict(int)
        for i in range(len(nums)):
            t = target - nums[i]
            if t in counts:
                return [counts[t], i]
            counts[nums[i]] = i

        return []