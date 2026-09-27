import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        q = deque()
        heapq.heapify(maxHeap)
        time = 0
        while q or maxHeap:
            time += 1
            if maxHeap:
                amount_left = heapq.heappop(maxHeap) + 1
                if amount_left != 0:
                    q.append([amount_left, time + n])
            if q:
                if time == q[0][1]:
                    heapq.heappush(maxHeap, q.popleft()[0])

        return time