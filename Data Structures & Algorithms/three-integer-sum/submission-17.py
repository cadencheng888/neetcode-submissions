class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            r = len(nums) - 1
            l = i + 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    result.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        return result