# PROBLEM LINK:- https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        expected = heights.copy()
        expected.sort()
        c = 0
        for i in range(0,n):
            if heights[i] != expected[i]:
                c += 1
        return c
