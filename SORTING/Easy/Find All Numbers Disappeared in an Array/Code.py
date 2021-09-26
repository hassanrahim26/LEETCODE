# PROBLEM LINK:- https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        v = []
        for i in range(0, len(nums)):
            x = abs(nums[i]) - 1
            if nums[x] > 0:
                nums[x] = -nums[x]
        for i in range(0, len(nums)):
            if nums[i] > 0:
                v.append(i+1)
        return v
