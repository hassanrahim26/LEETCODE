# PROBLEM LINK:- https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        while(start <= end):
            mid = start + (end - start)//2
            target = self.count(nums, mid)
            if target == mid:
                return mid
            elif target > mid:
                start = mid + 1
            else:
                end = mid - 1
        return -1
    
    def count(self, nums: List[int], x) -> int:
        c = 0
        for i in nums:
            if i >= x:
                c += 1
        return c
            
