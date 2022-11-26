## [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

* **C++**
```cpp
class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        auto comp = [&endTime](const int i1, const int i2) {return endTime[i1] < endTime[i2];};
        int n = endTime.size();
        vector<int> index(n);
        iota(index.begin(), index.end(), 0);
        sort(index.begin(), index.end(), comp);
        
        vector<int> endSorted(endTime.begin(), endTime.end());
        sort(endSorted.begin(), endSorted.end());
        
        vector<int> dp(n+1);
        for(int i = 1; i <= n; i++){
            int j = upper_bound(endSorted.begin(), endSorted.end(), startTime[index[i-1]]) - endSorted.begin();
            dp[i] = max(dp[i-1], profit[index[i-1]] + dp[j]);
        }
        return dp[n];
    }
};
```
