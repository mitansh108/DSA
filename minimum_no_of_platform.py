class Solution:
    def findPlatform(self, Arrival, Departure):
        #your code goes here
        Arrival.sort()
        Departure.sort()
        i = 1 
        j = 0
        ans = 1
        count = 1
        while i < len(Arrival):
            if Arrival[i] <= Departure[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            ans = max(ans, count)
        return ans