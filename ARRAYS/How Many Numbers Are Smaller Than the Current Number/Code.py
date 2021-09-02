#PROBLEM LINK:- https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, v):
        n = len(v)
        r = []
        for i in range(0,n):
            c = 0
            for j in range(0,n):
                if(j != i and v[j] < v[i]):
                    c += 1
            r.append(c)
        return r
