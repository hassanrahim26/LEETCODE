# PROBLEM LINK:- https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, 10 ** 9
        while low < high:
            mid, val = low + (high-low)//2, 0
            
            for x in piles:
                val = val + (x+mid-1)//mid
            
            if val <= h:
                high = mid
            else:
                low = mid+1
                
        return low
