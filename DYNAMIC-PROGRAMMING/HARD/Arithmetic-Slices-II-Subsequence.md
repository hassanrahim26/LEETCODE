## [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)

* **C++**
```cpp
class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        vector<unordered_map<long long, int>> dp(n);
        for(int i = 1; i < n; i++){
            for(int j = 0; j < i; j++){
                long long diff = (long long) nums[i] - nums[j];
                int c = dp[j].count(diff) ? dp[j][diff] : 0;
                dp[i][diff] += c+1;
                ans += c;
            }
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                c = 0
                if diff in dp[j]:
                    c = dp[j][diff]
                
                dp[i][diff] += c+1
                ans += c
        return ans
```
