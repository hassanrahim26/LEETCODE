/*
PROBLEM LINK:- https://leetcode.com/problems/guess-number-higher-or-lower/
*/

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int start = 1, end = n;
        while(start <= end)
        {
            int mid = start + (end - start)/2;
            int ans = guess(mid);
            if(ans == 0)
                return mid;
            else if(ans == 1)
                start = mid + 1;
            else
                end = mid;
        }
        return 0;
    }
};
