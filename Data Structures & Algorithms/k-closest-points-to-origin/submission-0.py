import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums_dict = collections.defaultdict(list)
        nums = []
        heapq.heapify(nums)
        for coord in points:
            print("hi")
            x, y = coord[0], coord[1]
            distance = math.sqrt(x * x + y * y)
            nums_dict[distance].append([x, y])
            heapq.heappush(nums, distance)
        print(nums_dict)
        print(nums)
        result = []
        for i in range(k):
            dist = heapq.heappop(nums)
            result.append(nums_dict[dist].pop())
        print(result)
        return result