/*
PROBLEM LINK:- https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
*/

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& c, int e) {
         int n = c.size();
         int x = *max_element(c.begin(),c.end());
         vector<bool> result(n);
         for(int i = 0; i < n; i++)
         {
             if(c[i]+e>=x)
             {
                 result[i] = true;
             }
             else
                 result[i] = false;
         }
         return result;
    }
};
