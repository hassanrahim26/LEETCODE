## [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

* **C++**
```cp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0, n = nums.size(), res = n + 1;
        for(int j = 0; j < n; j++)
        {
            target -= nums[j];
            while(target <= 0)
            {
                res = min(res, j - i + 1);
                target += nums[i++];
            }
        }
        
        return res % (n + 1);
    }
};
```
* **Python**
```py
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        res = len(nums) + 1
        for j in range(0, len(nums)):
            target -= nums[j]
            while(target <= 0):
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)
```
