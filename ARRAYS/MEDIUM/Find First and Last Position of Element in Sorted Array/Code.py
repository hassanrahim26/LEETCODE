# PROBLEM LINK:- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = self.BinarySearch(nums, target)
        b = self.BinarySearch(nums, target + 1) - 1
        if a < len(nums) and nums[a] == target:
            return [a, b]
        else:
            return [-1, -1]
        
    def BinarySearch(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
