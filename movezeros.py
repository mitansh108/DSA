# Move Zeros: two-pointer approach
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        
        """
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l+=1
