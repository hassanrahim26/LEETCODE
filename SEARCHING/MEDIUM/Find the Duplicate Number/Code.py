# PROBLEM LINK:- https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = low + (high - low)//2
            c = 0
            
            for x in nums:
                if x <= mid:
                    c += 1
            
            if c <= mid:
                low = mid + 1
            else:
                high = mid - 1
        
        return low 
