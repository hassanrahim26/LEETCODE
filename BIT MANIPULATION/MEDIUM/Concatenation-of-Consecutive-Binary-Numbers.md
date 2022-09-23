## [Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)

* **C++**
```cpp
class Solution {
public:
    int concatenatedBinary(int n) {
        long long ans = 0, mod = 1e9+7, c = 0;
        for(int i = 1; i <= n; i++){
            if((i & (i-1)) == 0)
                c++;
            ans = ((ans << c) + i) % mod;
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, c, mod = 0, 0, 10**9 + 7
        for i in range(1, n+1):
            if i & (i-1) == 0:
                c += 1
            ans = ((ans << c) + i) % mod
        return ans
```
