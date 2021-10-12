# PROBLEM LINK:- https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        v = []
        
        for i in range(0, len(nums1)):
            v.append(nums1[i])
            
        for j in range(0, len(nums2)):
            v.append(nums2[j])
            
        v.sort()
        x = len(v)
        
        if x % 2 == 0:
            return (v[int(x/2) - 1] + v[int(x/2)])/2
        return v[int(x/2)]
