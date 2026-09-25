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
            r = [heapq.heappop(heap)]
            print(r)
            result.append([r[0][1], r[0][2]])
        return result