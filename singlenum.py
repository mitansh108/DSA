class Solution(object):
    def singleNumber(self, nums):
        ans = {}
        n = len(nums)

        for i in range(n):
            val = nums[i]

            if val in ans:
                ans[val] +=1
            else:
                ans[val] = 1
        
        for key, value in ans.items():
            if value ==1:
                return key
    

