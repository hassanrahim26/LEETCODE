
# PROBLEM LINK:- https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        d = 0
        for i in nums:
            c = 0
            while i > 0:
                i //= 10
                c += 1
            if c % 2 == 0:
                d += 1
        return d
