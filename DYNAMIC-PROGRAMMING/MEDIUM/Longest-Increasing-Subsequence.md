## [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

* **C++**
```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < i; j++)
                if(nums[i] > nums[j] and dp[i] < dp[j] + 1)
                    dp[i] = dp[j] + 1;
        
        return *max_element(dp.begin(), dp.end());
    }
};
```

* **Python**
```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp)
```
