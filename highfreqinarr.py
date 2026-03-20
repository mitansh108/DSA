class Solution:
    def mostFrequentElement(self, nums):
        count = {}

        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n] = 1
        
        maxfrequency = 0
        ans = 0

        for key, value in count.items():
            if value > maxfrequency:
                maxfrequency = value
                ans = key

        return ans

       
        