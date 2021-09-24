# PROBLEM LINK:- https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)
        while(start < end):
            mid = start + (end - start)//2
            if arr[mid] > arr[mid+1]:
                end = mid
            else:
                start = mid + 1
        return start
