#PROBLEM LINK:- https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, c, e):
        result = []
        for i in range(len(c)):
            if c[i]+e>=max(c):
                result.append(True)
            else:
                result.append(False)
        return result
