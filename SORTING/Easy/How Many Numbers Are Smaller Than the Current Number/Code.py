# PROBLEM LINK:- https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        v = []
        for i in range(0,n):
            c = 0
            for j in range(0,n):
                if(i != j and nums[i] > nums[j]):
                    c += 1
            v.append(c)
        return v
