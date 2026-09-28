from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        tasks_count = [-i for i in count.values()]
        heapq.heapify(tasks_count)
        q = deque()
        time = 0
        while tasks_count or q:
            time += 1
            if tasks_count:
                new_time = heapq.heappop(tasks_count) + 1
                if new_time != 0:
                    q.append([new_time, n + time])
            if q:
                if time == q[0][1]:
                    heapq.heappush(tasks_count, q.popleft()[0])
        return time