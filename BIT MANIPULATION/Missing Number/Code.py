# PROBLEM LINK:- https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        for x in nums:
            n ^= x;
            n ^= i
            i += 1
        return n
        
