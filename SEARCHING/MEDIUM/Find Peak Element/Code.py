# PROBLEM LINK:- https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1;
        while(start < end):
            mid = start + (end - start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
        return start
