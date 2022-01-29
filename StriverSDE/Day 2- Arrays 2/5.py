# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        s = (n*(n+1))//2
        s2 = (n*(n+1)*(2*n+1))//6
        k = sum(A)
        k2 = 0
        for i in range(n):
            k2 += (A[i]**2)
        p = s-k
        q = (s2-k2)//p
        return [(q-p)//2, (p+q)//2]
