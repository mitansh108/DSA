class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        ans = {}

        for i in range(n):
            val = nums[i]
            if val in ans:
                return True
            ans[val] = True

        return False