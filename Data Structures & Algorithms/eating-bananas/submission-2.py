import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_speed = right # Default to the max speed
        
        while left <= right:
            k = (left + right) // 2 # Check the middle speed
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                
            if hours <= h:
                # She finished in time! Save this speed as a potential answer.
                best_speed = k
                # Now see if she can go even slower by checking the lower half.
                right = k - 1
            else:
                # She was too slow. We must check the upper half for a faster speed.
                left = k + 1
                
        return best_speed