class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
        count = 0
        div = 0
        
        while A > 0:
            div = A //5
            count = count + div
            A = A //5
        
        return count
            