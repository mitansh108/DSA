
from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        task_heap = [-n for n in count.values()]
        heapq.heapify(task_heap)

        time = 0
        q = deque() #pairs of [-cnt, idealTime]

        while task_heap or q:
            time+=1

            if task_heap:
                cnt = 1 + heapq.heappop(task_heap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heapq.heappush(task_heap, q.popleft()[0])
        return time

       



        