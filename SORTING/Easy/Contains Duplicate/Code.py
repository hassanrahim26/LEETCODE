# PROBLEM LINK:- https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        n = len(nums)
        nums.sort()
        for i in range(1,n):
            if nums[i-1] == nums[i]:
                return True;
        return False;
