class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0

        while A > 0:
            A = A // 5
            count += A

        return count
