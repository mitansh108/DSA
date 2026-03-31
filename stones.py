import heapq
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            first = abs(first)
            second = abs(second)

            if second < first:
                heapq.heappush(stones, second-first)
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
        
        


        