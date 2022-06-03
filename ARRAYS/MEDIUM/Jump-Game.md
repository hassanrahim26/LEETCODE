## [Jump Game](https://leetcode.com/problems/jump-game/)

* **C++**
```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int step = nums[0], i = 1;
        while(i < nums.size()){
            step--;
            if(step < 0)
                return false;
            
            if(nums[i] > step)
                step = nums[i];
            i++;
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = nums[0]
        i = 1
        
        while i < len(nums):
            step -= 1
            
            if step < 0:
                return False
            
            if nums[i] > step:
                step = nums[i]
            
            i += 1
        
        return True
```
