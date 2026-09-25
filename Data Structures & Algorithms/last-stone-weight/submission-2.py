from heapq import heappop, heapify, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
       
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if y == x:
                continue
            if y < x:
                heappush(stones, y-x)
        if stones:
            return -1 * stones[0]
        return 0