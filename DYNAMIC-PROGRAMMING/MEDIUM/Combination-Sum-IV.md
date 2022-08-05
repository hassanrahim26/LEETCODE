## [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

* **C++**
```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int t) {
        vector<unsigned int> dp(t+1, 0);
        dp[0] = 1;
        for(int i = 1; i <= t; i++)
            for(int x: nums)
                if(x <= i)  dp[i] += dp[i-x];
        return dp[t];
    }
};
```

* **PYTHON**
```py
class Solution:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        dp = [0]*(t+1)
        dp[0] = 1
        for i in range(1, t+1):
            for x in nums:
                if x <= i:  dp[i] += dp[i-x]
        return dp[t]
```
