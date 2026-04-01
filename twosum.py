# Two Sum: use a hash map for O(n) time complexity
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        n = len(nums)
        ans = {}

        for i in range (n):
            val = nums[i]
            partner = target - val

            if partner in ans:
                return[ans[partner], i]
            
            else:
                ans[val] = i

    
        

        
            

        
        
