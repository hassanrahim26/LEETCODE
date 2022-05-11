## [Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/)

* **C++**
```cpp
class Solution {
public:
    int countVowelStrings(int n) {
        vector<int> dp(5, 1);
        int ans = 0;
        
        while(--n){
            for(int i = 3; i >= 0; i--)
                dp[i] += dp[i+1];
        }
        
        for(auto x: dp)
            ans += x;
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        
        for x in range(n-1):
            for i in range(1, 5):
                dp[i] += dp[i-1]
        
        return sum(dp)
```
