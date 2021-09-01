#PROBLEM LINK:- https://leetcode.com/problems/richest-customer-wealth/submissions/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts = [sum(wealth) for wealth in accounts]
        return max(accounts)
