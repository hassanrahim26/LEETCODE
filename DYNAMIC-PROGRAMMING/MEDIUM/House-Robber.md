## [House Robber](https://leetcode.com/problems/house-robber/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
      int rob(vector<int>& nums) {
          if(nums.size() == 0) return 0;
          int prev1 = 0, prev2 = 0;
          for(auto x: nums){
              int temp = prev1;
              prev1 = max(prev1, prev2 + x);
              prev2 = temp;
          }
          return prev1;
      }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int rob(vector<int>& nums) {
          int n = nums.size();
          int dp[n+1];
          dp[0] = 0;
          dp[1] = nums[0];
          for(int i = 2; i <= nums.size(); i++){
              dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
          }
          return dp[n];
      }
  };
  ```
  
<hr>

* **PYTHON**

  * 1
  ```py
  class Solution:
      def rob(self, nums: List[int]) -> int:
          if(len(nums) == 0): return 0
          prev1, prev2 = 0, 0
          for x in nums:
              temp = prev1
              prev1 = max(prev1, prev2 + x)
              prev2 = temp
          return prev1
  ```
  
  * 2
  ```py
  class Solution:
      def rob(self, nums: List[int]) -> int:
          n = len(nums)
          dp = [0]*(n+1)
          dp[0] = 0
          dp[1] = nums[0]
          for i in range(2, n+1):
              dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
          return dp[n]
  ```
  
  
