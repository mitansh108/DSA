class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        
        #lets move bottom left
        row = A-1 
        column = B-1
        
        while row >=1 and column >=1:
            ans +=1
            row -=1
            column -=1
            
        #lets move bottom right
        row = A-1
        column = B+1
        while row >=1 and column <=8:
            ans +=1
            row -=1
            column +=1
            
        #lets move top left
        row = A+1 
        column = B-1
        while row <=8 and column >=1:
            ans +=1
            row +=1
            column -=1
        
        #lets move bottom left
        row = A+1 
        column = B+1
        while row <=8 and column <=8:
            ans +=1
            row +=1
            column +=1
            
        return ans
    
        
           
           
       
            
