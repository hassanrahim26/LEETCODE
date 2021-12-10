# PROBLEM LINK:- https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x
