class Solution:
    def candy(self, ratings: List[int]) -> int:
        #three while loops first for checking if the surface is flat
        #second for uphill and third for downhill

        
        i = 1
        n = len(ratings)
        res = n

        while i < n:
            if ratings[i] == ratings[i-1]:
                i+=1
                continue

            peak = 0
            while i<n and ratings[i] > ratings[i-1]:
                peak+=1
                res+=peak
                i+=1
            
            down = 0
            while i < n and ratings[i] < ratings[i-1]:
                down+=1
                res+=down
                i+=1
            
            res -= min(peak, down)
                
        return res


        