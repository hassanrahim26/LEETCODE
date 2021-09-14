
#PROBLEM LINK:- https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(self, v):
        c = 0;
        n = len(v)
        for i in range(0,n):
            for j in range(1,n):
                if(i < j and v[i] == v[j]):
                    c += 1
        return c
