class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num - 1 not in nums_set:
                current_longest = 0
                while current_num in nums_set:
                    current_longest += 1
                    current_num += 1
                longest = max(current_longest, longest)

        return longest
            


