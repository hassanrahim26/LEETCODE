# PROBLEM LINK:- https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, v1, v2):
        n = len(v2)
        r = []
        for i in range(0,n):
            r.insert(v2[i], v1[i])
        return r
