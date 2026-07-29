class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        max_count = 0
        for num in nums:
            current = num
            while current in nums:
                count += 1
                current += 1
            if count > max_count:
                max_count = count
            count = 0
        return max_count

        