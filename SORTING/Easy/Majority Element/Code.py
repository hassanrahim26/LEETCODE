# PROBLEM LINK:- https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[int(n/2)]
