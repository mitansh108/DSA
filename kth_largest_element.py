import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        target = n - k
        heapq.heapify(nums)

        for i in range(1, target+1):
            ans = heapq.heappop(nums)

        return nums[0]
        
        