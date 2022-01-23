/*
PROBLEM LINK:- https://leetcode.com/problems/koko-eating-bananas/
*/

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1, high = INT_MIN;
        
        for(auto x: piles)
            high = max(x, high);

        while(low<high)
        {
            int mid = low + (high-low)/2, val = 0;
            
            for(auto x: piles)    
                val += (x + mid - 1)/mid;
            
            if(val <= h)
                high = mid;
            else
                low = mid+1;
        }
        
        return low;
    }
};          
