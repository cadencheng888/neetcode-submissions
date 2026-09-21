class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)
        holder = 1
        for i in range(1, len(nums), 1):
            holder = nums[i - 1] * holder
            left_product[i] = holder
        holder = 1
        for i in range(len(nums) - 2, -1, -1):
            holder = nums[i + 1] * holder
            right_product[i] = holder
        result = []
        for i in range(len(nums)):
            result.append(right_product[i] * left_product[i])
        return result
