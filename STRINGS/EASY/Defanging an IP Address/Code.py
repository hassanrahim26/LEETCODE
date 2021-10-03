# PROBLEM LINK:- https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ""
        for i in address:
            if i == '.':
                s += "[.]"
            else:
                s += i
        return s
        
