# PROBLEM LINK:- https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for c in s + t:
            r ^= ord(c)
        return chr(r)
