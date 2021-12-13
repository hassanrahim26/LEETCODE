# PROBLEM LINK:- https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, v: List[List[int]]) -> int:
        n = len(v)
        m = len(v[0])
        i = n - 1
        j = 0
        count = 0
        
        while(i >= 0 and i < n and j >= 0 and j < m):
            if v[i][j] < 0:
                count += m - j
                i -= 1
            else:
                j += 1
        return count
