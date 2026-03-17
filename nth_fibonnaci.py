class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Base case
        if A <= 2:
            return 1
            
        a = 1
        b = 1
        
        for i in range(3, A + 1):
            # Use parentheses to modulo the WHOLE sum
            temp = (a + b) % 1000000007
            a = b
            b = temp
            
        # Return the final calculated value
        return b