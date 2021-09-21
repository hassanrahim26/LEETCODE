# PROBLEM LINK:- https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(0,len(arr)):
            for j in range(0, len(arr)):
                if arr[i] == 2 * arr[j] and i != j:
                    return True
        return False
