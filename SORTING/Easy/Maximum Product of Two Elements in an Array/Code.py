# PROBLEM LINK:- https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return (nums[n-1]-1) * (nums[n-2]-1)
