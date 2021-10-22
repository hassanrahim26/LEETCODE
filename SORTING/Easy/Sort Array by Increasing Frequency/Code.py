# PROBLEM LINK:- https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        return sorted(nums, key = nums.count)
        
