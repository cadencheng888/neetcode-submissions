class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in nums_dict:
                
                return [nums_dict[target_num], i]
            nums_dict[nums[i]] = i
            