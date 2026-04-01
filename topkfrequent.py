# Top K Frequent: use a heap for O(n log k)
import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []
        
        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val,key))
            else:
                heapq.heappushpop(heap, (val,key))
        return [h[1] for h in heap]
