# PROBLEM LINK:- https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        d = 0
        while(num > 0):
            if num % 2 == 0:
                num /= 2
                c+=1
            else:
                num -= 1
                d+=1
        return c + d
