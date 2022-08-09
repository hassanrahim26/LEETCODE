## [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/)

* **C++**
```cpp
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& v) {
        long res = 0, mod = 1e9 + 7;
        sort(v.begin(), v.end());
        unordered_map<int, long> dp;
        
        for(int i = 0; i < v.size(); i++){
            dp[v[i]] = 1;
            for(int j = 0; j < i; j++)
                if(v[i] % v[j] == 0)
                    dp[v[i]] = (dp[v[i]] + dp[v[j]] * dp[v[i] / v[j]]) % mod;
            res = (res + dp[v[i]]) % mod;
        }
        return res;
    }
};
```

* **PYTHON**
```py
class Solution:
    def numFactoredBinaryTrees(self, v: List[int]) -> int:
        v.sort()
        mod = 10**9 + 7
        dp = {}
        
        for x in v:
            dp[x] = 1
        
        for i, n in enumerate(v):
            for j in range(i):
                if not (n % v[j]) and n//v[j] in dp:
                    dp[n] += dp[v[j]] * dp[n//v[j]]
                    dp[n] %= mod
        
        return sum(dp.values()) % mod
```
