# PROBLEM LINK:- https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        a = 1e-6
        low = 1
        high = x
        while high - low > a:
            mid = (high + low)/2
            if mid * mid < x:
                low = mid
            else:
                high = mid
        return int(high)
