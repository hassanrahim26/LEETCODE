## [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)

* **C++**
```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int n = nums.size(), m = multipliers.size();
        vector<int> dp(m+1);
        
        for(int i = 0; i < m; i++){
            int p = multipliers[m-1-i];
            for(int j = 0; j < m - i; j++){
                dp[j] = max(p * nums[j] + dp[j+1], p * nums[j + (n - (m - i))] + dp[j]);
            }
        }
        return dp[0];
    }
};
```

* **PYTHON**
```py
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [0]*(m+1)
        
        for i in range(m):
            p = multipliers[m-1-i]
            for j in range(m-i):
                dp[j] = max(p * nums[j] + dp[j+1], p * nums[j + (n - (m-i))] + dp[j])
                
        return dp[0]
```
