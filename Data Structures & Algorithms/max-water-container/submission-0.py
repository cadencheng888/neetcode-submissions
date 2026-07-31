class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                water = min(heights[j], heights[i]) * (j - i)
                
                if water > maxWater:
                    print(water)
                    print(i, j)
                    maxWater = water
        return maxWater