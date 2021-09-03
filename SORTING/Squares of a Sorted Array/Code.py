# PROBLEM LINK:- https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, v):
        n = len(v)
        for i in range(0,n):
            v[i] *= v[i]
        v.sort()
        return v
