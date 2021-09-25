# PROBLEM LINK:- https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0
        end = n
        while(start <= end):
            mid = start + (end - start)//2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == 1:
                start = mid + 1
            else:
                end = mid
        return 0
