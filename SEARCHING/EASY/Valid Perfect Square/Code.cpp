/*
PROBLEM LINK:- https://leetcode.com/problems/valid-perfect-square/
*/

class Solution {
public:
    bool isPerfectSquare(int num) {
        int start = 1, end = num;
        
        while(start <= end)
        {
            long long int mid = start + (end - start)/2;
            
            if(mid * mid == num)
                return true;
            else if(mid * mid < num)
                start = mid + 1;
            else
                end = mid - 1;
        }
        
        return false;
    }
};
