## [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

* **C++**

  * 1
  ```cpp
  class Solution {
  public:
       int maxSubarraySumCircular(vector<int>& nums) {
           int totalSum = 0, maxSum = INT_MIN, curMax = 0, minSum = INT_MAX, curMin = 0;
           for (int x : nums){
               curMax = max(x, curMax + x);  
               maxSum = max(maxSum, curMax); 
               curMin = min(x, curMin + x); 
               minSum = min(minSum, curMin); 
               totalSum += x;
           }
           return maxSum > 0 ? max(maxSum, totalSum - minSum) : maxSum;
       }
  };
  ```
  
  * 2
  ```cpp
  class Solution {
  public:
      int maxSubarraySumCircular(vector<int>& nums) {
          int s = accumulate(nums.begin(), nums.end(), 0);
          int res = nums[0], maxSub = nums[0], minSub = 0;
        
          for(int i = 1; i < nums.size(); i++){
             maxSub = max(maxSub + nums[i], nums[i]);
             minSub = min(minSub + nums[i], nums[i]);
             res = max(res, max(maxSub, s - minSub));
          }
          return res;
      }
  };
  ```

<hr>

* **PYTHON**
```py
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        res = nums[0]
        maxSub = nums[0]
        minSub = 0
        for i in range(1,len(nums)):
            maxSub = max(maxSub+nums[i], nums[i])
            minSub = min(minSub+nums[i], nums[i])
            res = max(res, maxSub, s - minSub)
        return res
```
