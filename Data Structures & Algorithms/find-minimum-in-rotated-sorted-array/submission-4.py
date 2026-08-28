class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[r] > nums[l]:
                result = min(result, nums[l])
                return result
            result = min(result, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
                print(m)
                print(l)
                print(r)
            else:
                r = m - 1
        return result