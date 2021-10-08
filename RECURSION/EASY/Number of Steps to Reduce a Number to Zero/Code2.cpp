/*
PROBLEM LINK:- https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
*/

class Solution {
public:
    int numberOfSteps (int num) {
        if(num < 2)
            return num;
        if(num & 1)
            return numberOfSteps(num-1)+1;
        
        return numberOfSteps(num/2)+1;
    }
};
