class Solution:
    def majorityElement(self, nums):
        
        n = len(nums)
        ans = {}
        for i in range(n):
            val = nums[i]

            if val in ans:
                ans[val]+=1
            else:
                ans[val] = 1
        
        return max(ans, key=ans.get)