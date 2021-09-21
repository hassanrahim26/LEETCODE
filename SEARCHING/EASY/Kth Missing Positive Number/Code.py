# PROBLEM LINK:- https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(0, len(arr)):
            if arr[i] <= k:
                k += 1
        return k
        
