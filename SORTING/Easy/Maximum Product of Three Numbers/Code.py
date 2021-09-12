# PROBLEM LINK:- https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        a = nums[n-1] * nums[n-2] * nums[n-3]
        b = nums[0] * nums[1] * nums[n-1]
        return max(a,b)
