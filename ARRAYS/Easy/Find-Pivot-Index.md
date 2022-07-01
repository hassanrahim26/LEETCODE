## [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

* **C++**
```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int s = 0, ls = 0;
        for(auto x: nums)
            s += x;
        
        for(int i = 0; i < nums.size(); i++)
        {
            if(ls == s - nums[i])
                return i;
            else
            {
                ls += nums[i];
                s -= nums[i];
            }
        }
        
        return -1;
    }
};
```

* **Python**
```py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s, ls = 0, 0
        for x in nums:
            s += x
        
        for i in range(0, len(nums)):
            if ls == s - nums[i]:
                return i
            else:
                ls += nums[i]
                s -= nums[i]
        
        return -1
```
