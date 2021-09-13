# PROBLEM LINK:- https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, v):
        n = len(v)
        x = 0
        y = 0
        for i in range(0,n):
            x += v[i]
            y = max(y,x)
        return y
