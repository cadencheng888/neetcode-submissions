class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {word: index for index, word in enumerate(nums)}
        result = []
        i = 0
        for num in nums:
            if ((target - num) in my_dict) and (i != my_dict[target-num]):

                result.append(i)
                result.append(my_dict[target-num])
                break
            i = i + 1
        return result