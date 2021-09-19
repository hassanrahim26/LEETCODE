# PROBLEM LINK:- https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1;
        while(num > 0):
            num -= i
            i += 2
        return num == 0
        
