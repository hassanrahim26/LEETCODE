# PROBLEM LINK:- https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        res = 0
        sum = 0
        while sum < target or (sum - target)%2 != 0:
            res += 1
            sum += res
        return res
        
