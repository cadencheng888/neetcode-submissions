class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        slow = 0
        needd = 0
        my_set = set(numbers)
        for i in range(len(numbers)):
            needed = target - numbers[i]
            if needed in my_set:
                result.append(i + 1)
                break
        for i in range(len(numbers)):
            if numbers[i] == needed:
                result.append(i + 1)
        return result
