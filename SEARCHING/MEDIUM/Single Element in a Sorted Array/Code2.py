# PROBLEM LINK:- https://leetcode.com/problems/single-element-in-a-sorted-array/


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 2
        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid] == nums[mid^1]:
                low = mid + 1
            else:
                high = mid - 1
                
        return nums[low]
