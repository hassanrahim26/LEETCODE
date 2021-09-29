# PROBLEM LINK:- https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        v = []
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                v.append(nums[i])
        for i in range(0, len(nums)):
            if nums[i] % 2 != 0:
                v.append(nums[i])
        return v
            
