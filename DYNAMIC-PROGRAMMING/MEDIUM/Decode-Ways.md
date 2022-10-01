## [Decode Ways](https://leetcode.com/problems/decode-ways/)

* **C++**
  * 1
  ```cpp
  class Solution {
  public:
      int numDecodings(string s) {
          int n = s.size();
          vector<int> dp(n+1);
          dp[n] = 1;
          for(int i = n-1; i >= 0; i--){
              if(s[i] == '0'){
                  dp[i] = 0;
              }
              else{
                  dp[i] = dp[i+1];
                  if(i < n-1 and (s[i] == '1' || s[i] == '2' and s[i+1] <= '6'))
                      dp[i] += dp[i+2];
              }
          }
          return s.empty() ? 0 : dp[0];
      }
  };
  ```
  * 2
  ```cpp
  class Solution {
  public:
      int numDecodings(string s) {
          int n = s.size(), dp = 0, dp1 = 1, dp2 = 0;
          for(int i = n - 1; i >= 0; --i){
              if(s[i] != '0')
                  dp += dp1;
              if(i+1 < s.size() && (s[i] == '1' || s[i] == '2' && s[i+1] <= '6'))
                  dp += dp2;
              dp2 = dp1;
              dp1 = dp;
              dp = 0;
          }
          return dp1;
      }
  };
  ```
<hr>

* **Python**
  * 1
  ```py
  class Solution:
  def numDecodings(self, s: str) -> int:
      n = len(s)
      dp = [None]*(n+1)
      dp[n] = 1
      for i in range(n-1, -1, -1):
          if(s[i] == '0'):
              dp[i] = 0
          else:
              dp[i] = dp[i+1]
              if(i < n-1 and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6')):
                  dp[i] += dp[i+2]
      return 0 if len(s) == 0 else dp[0]
  ```
  
  * 2
  ```py
  class Solution:
  def numDecodings(self, s: str) -> int:
      n, dp, dp1, dp2 = len(s), 0, 1, 0
      for i in range(n-1, -1, -1):
          if s[i] != '0':
              dp += dp1
          if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
              dp += dp2
          dp, dp1, dp2 = 0, dp, dp1
      return dp1
  ```
