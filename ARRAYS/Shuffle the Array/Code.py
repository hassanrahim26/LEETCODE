#PROBLEM LINK:- https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums, n): 
        v = []
        for i in range(n):
            v.append(nums[i])
            v.append(nums[i+n])
        return v
