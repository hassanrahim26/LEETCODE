## [Perfect Squares](https://leetcode.com/problems/perfect-squares/)

* **C++**
```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        int count = 1;
        while(count * count <= n){
            int sq = count * count;
            for(int i = sq; i < n+1; i++){
                dp[i] = min(dp[i-sq]+1, dp[i]);
            }
            count++;
        }
        return dp[n];
    }
};
```
* **Python**
```py
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        squares = [i**2 for i in range(2, n) if i**2 <= n]
        dp[0] = 0
        count = 1
        while(count * count <= n):
            sq = count * count
            for i in range(sq, n+1):
                dp[i] = min(dp[i-sq] + 1, dp[i])
            count += 1
        return dp[-1]
```
