import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coord in points:
            x, y = coord[0], coord[1]
            d = math.sqrt(x * x + y * y)
            heap.append([d, x, y])

        heapq.heapify(heap)

        result = []
        for i in range(k):
            d, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result