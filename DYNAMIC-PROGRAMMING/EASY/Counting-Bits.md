## [Counting Bits](https://leetcode.com/problems/counting-bits/)

* **C++**
```cpp
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1);
        dp[0] = 0;
        for(int i = 1; i < n+1; i++)
        {
            dp[i] = dp[i/2] + i%2;
        }
        return dp;
    }
};
```

* **Python**
```py
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        for i in range(1, n+1):
            if i%2 == 1:
                dp.append(dp[i-1] + 1)
            else:
                dp.append(dp[i//2])
        return dp
```
