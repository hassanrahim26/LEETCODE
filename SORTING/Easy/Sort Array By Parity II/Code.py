# PROBLEM LINK:- https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 2
            else:
                j += 2
        return nums
        
