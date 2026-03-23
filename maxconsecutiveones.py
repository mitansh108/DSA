class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        max_num = 0
        l = 0
        for r in range(n):
            if nums[r] == 1:
                l +=1
            else:
                max_num = max(max_num, l)
                l = 0
        return max(max_num, l)
        
        
        