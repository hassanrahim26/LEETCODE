# PROBLEM LINK:- https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i-1] == nums[i]:
                return nums[i]
        return -1
