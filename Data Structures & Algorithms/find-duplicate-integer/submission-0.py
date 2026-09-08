class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            if nums_dict[num] == 2:
                return num
        
        