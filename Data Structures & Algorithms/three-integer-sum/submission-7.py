class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            slow = i + 1
            fast = len(nums) - 1
            while slow < fast:
                total = nums[i] + nums[slow] + nums[fast]
                print(i, slow, fast, total)
                if total == 0:
                    triple = [nums[i], nums[slow], nums[fast]]
                    result.append(triple)
                    slow += 1
                    while slow < fast and nums[slow] == nums[slow - 1]:
                        slow += 1
                elif total < 0:
                    slow += 1
                else:
                    fast -= 1
        return result
            
