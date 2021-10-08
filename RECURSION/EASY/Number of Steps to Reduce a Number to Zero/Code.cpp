/*
PROBLEM LINK:- https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
*/

class Solution {
public:
    int numberOfSteps(int num) {
        int c = 0, d = 0;
        while(num > 0)
        {
            if(num % 2 == 0)
            {
                num /= 2;
                c++;
            }
            else
            {
                num -= 1;
                d++;
            }
        }
        return c + d;
    }
};
