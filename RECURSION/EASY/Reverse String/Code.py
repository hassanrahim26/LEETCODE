# PROBLEM LINK:- https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(a, b, s):
            if a >= b:
                return
            else:
                s[a], s[b] = s[b], s[a]
                reverse(a+1, b-1, s)
        reverse(0, len(s) - 1, s)
