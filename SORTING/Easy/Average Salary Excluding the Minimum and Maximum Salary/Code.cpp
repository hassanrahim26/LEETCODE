/*
PROBLEM LINK:- https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
*/

class Solution {
public:
    double average(vector<int>& salary) {
        double sum = 0.00;
        int n = salary.size();
        sort(salary.begin(), salary.end());
        for(int i = 0; i < n; i++) 
        {
            sum += salary[i];
        }
        double avg = sum - (salary[0] + salary[n-1]);
        return avg/(n-2);
    }
};
