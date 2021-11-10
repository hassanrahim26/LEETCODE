# https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xffffffff
        # python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit
        
        while(b & x > 0):
            c = (a & b) << 1
            a ^= b
            b = c 
        return (a & x) if b > 0 else a
