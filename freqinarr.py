class Solution:
    def countFrequencies(self, nums: list[int]) -> list[list[int]]:

        count = {}

        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n] = 1

        ans = []
        for key, value in count.items():
            ans.append([key,value]) 
        
        return ans
        

        # Your code goes here
