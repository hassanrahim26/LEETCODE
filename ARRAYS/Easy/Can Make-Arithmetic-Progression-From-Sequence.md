## [Can Make Arithmetic Progression From Sequence](https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/)

* **C++**
```cpp
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int d = nums[1] - nums[0];
        
        for(int i = 2; i < nums.size(); i++)
        {
            if(nums[i] - nums[i-1] != d)
                return false;
        }
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def canMakeArithmeticProgression(self, nums: List[int]) -> bool:
        nums.sort()
        d = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] != d:
                return False
        return True
```
