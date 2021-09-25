# PROBLEM LINK:- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        v = []
        while(start < end):
            sum = nums[start] + nums[end]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                v.append(start+1)
                v.append(end+1)
                break
        return v
