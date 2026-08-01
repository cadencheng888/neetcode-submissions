class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow = 0
        fast = len(heights) - 1
        water = 0
        while slow < fast:
            water = max(min(heights[fast], heights[slow]) * (fast - slow), water)
            if heights[slow] > heights[fast]:
                fast -= 1
            else:
                slow += 1
            
        return water

                

            