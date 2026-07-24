class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max = 1
        count = 1
        print(nums)
        for i in range(len(nums) - 1):
            print(f"iteration {i}")
            if (nums[i + 1] == nums[i] + 1):
                count += 1
                print(f"iteration {i} count = {count}")
                if count > max:
                    max = count
                    print(f"iteration {i} max = {count}")
            elif (nums[i + 1] == nums[i]):
                continue
            else:
                count = 1
        return max
        