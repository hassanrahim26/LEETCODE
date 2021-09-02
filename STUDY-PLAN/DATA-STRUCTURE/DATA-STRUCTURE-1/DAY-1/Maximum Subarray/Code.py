# PROBLEM LINK:- https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, v: List[int]):
        n = len(v)
        m1 = v[0]
        m2 = v[0]
        for i in range(1,n):
            m1 = max(m1 + v[i], v[i])
            m2 = max(m1,m2)
        return m2
