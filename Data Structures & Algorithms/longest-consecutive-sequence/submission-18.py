class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        max_count = 0
        for num in nums:
            if num - 1 not in nums:
                current = num
                count = 1
                while current + 1 in nums:
                    count += 1
                    current += 1
                if max_count < count:
                    max_count = count
                count = 0
        return max_count

        