## [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/)

* **C++**
```cpp
class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        for(int i = 0; i < nums.size() - 1; i++)
        {
            if(nums[i] > nums[i+1])
            {
                if(i-1 >= 0 && nums[i-1] > nums[i+1])        
                    nums[i+1] = nums[i];
                else
                    nums[i] = nums[i+1];
                break;
            }
        }
        
        for(int i = 0; i < nums.size() - 1; i++)
        {
            if(nums[i] > nums[i+1])
                return false;
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                if i-1 >= 0 and nums[i-1] > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
                break
        
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        
        return True
```
