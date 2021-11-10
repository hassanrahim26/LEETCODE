/*
PROBLEM LINK:- https://leetcode.com/problems/sum-of-two-integers/
*/

class Solution {
public:
    int getSum(int a, int b) {
        while(b != 0)    
        {
            unsigned c = a & b;
            a ^= b;
            b = c << 1;
        }
        
        return a;
    }
};
