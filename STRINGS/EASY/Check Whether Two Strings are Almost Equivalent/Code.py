# PROBLEM LINK:- https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w = set(word1 + word2)
        for i in w:
            if abs(word1.count(i) - word2.count(i)) > 3:
                return False
            
        return True
