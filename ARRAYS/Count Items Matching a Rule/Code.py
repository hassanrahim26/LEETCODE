# PROBLEM LINK:- https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        n = len(items)
        c = 0
        
        if(ruleKey == "type"): x = 0
        if(ruleKey == "color"): x = 1
        if(ruleKey == "name"): x = 2
        
        for i in range(0,n):
            if(items[i][x] == ruleValue):
                c += 1
        return c
