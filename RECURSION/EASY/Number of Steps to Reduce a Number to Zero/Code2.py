# PROBLEM LINK:- https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num < 2:
            return num
        
        if num & 1:
            return self.numberOfSteps(num-1) + 1
        
        return self.numberOfSteps(num//2) + 1
