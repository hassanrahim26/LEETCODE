# PROBLEM LINK:- https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        v = []
        for i in range(1,n):
            if nums[i-1] == nums[i]:
                v.append(nums[i])
        return v
