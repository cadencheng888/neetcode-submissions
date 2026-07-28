class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        slow = 0
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    result.append(i + 1)
                    result.append(j + 1)
                    return result