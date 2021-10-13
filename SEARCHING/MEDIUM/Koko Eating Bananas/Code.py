# PROBLEM LINK:- https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = 1000000000
        while(l < r):
            m = l + (r-l) //2
            total = 0
            for p in piles:
                total += (p + m - 1) // m
            if total > h:
                l = m + 1
            else:
                r = m
        return l
