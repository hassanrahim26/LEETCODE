# PROBLEM LINK:- https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self,v):
        n = len(v)
        s = 0
        for i in range(0,n):
            s += v[i][i]
            if(i != n-i-1):
                s += v[i][n-i-1]
        return s
