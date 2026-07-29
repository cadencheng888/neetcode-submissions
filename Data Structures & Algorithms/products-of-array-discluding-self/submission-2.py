class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        result = [1] * len(nums)
        left_num = 1
        right_num = 1
        
        for i in range(1, len(nums)):
            left_num *= nums[i - 1]
            left_prod[i] = left_num
        for i in range(len(nums) - 2, -1, -1):
            right_num *= nums[i + 1]
            right_prod[i] = right_num
        for i in range(len(nums)):
            result[i] = left_prod[i] * right_prod[i]
        return result