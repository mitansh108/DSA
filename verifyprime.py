class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A<=1:
            return 0

        for n in range(2, int(A**0.5)+1):
            if A % n == 0:
                return 0

        return 1
