# PROBLEM LINK:- https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, v, x):
        n = len(v)
        r = []
        for i in range(0,n):
            for j in range(i+1,n):
                if(i != j and v[i] + v[j] == x):
                    r.append(i)
                    r.append(j)
        return r
