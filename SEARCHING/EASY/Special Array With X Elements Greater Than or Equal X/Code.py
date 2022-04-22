# PROBLEM LINK:- https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low)//2
            x = len(nums) - mid;
            
            if nums[mid] >= x:
                if mid == 0 or nums[mid-1] < x:
                    return x
                else:
                    high = mid - 1
            else:
                low = mid + 1
        
        return -1
