/*
PROBLEM LINK:- https://leetcode.com/problems/sqrtx/
*/

class Solution {
public:
    int mySqrt(int x) {
        double a = 1e-6;
        double low = 1, high = x, mid;
        while(high - low > a)
        {
            mid = (high + low)/2;
            if(mid * mid < x)
            {
                low  = mid;
            }
            else
            {
                high = mid;
            }
        }
        return high;
    }
};
