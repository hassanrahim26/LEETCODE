/*
PROBLEM LINK:- https://leetcode.com/problems/reach-a-number/
*/

class Solution {
public:
    int reachNumber(int target) {
        target = abs(target);
        int res = 0, sum = 0;
        while(sum < target || (sum - target)%2 != 0)
        {
            res++;
            sum += res;
        }
        return res;
    }
};
