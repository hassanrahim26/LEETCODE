# PROBLEM LINK:- https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = []
        for x in nums:
            if nums.count(x) == 1:
                s.append(x);
        return sum(s)
