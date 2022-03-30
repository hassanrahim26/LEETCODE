## [Move Zeroes](https://leetcode.com/problems/move-zeroes/)

* **C++**
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for(int i = 0, j = 0; i < nums.size(); i++)
        {
            if(nums[i])
                swap(nums[i], nums[j++]);
        }
    }
};
```

* **Python**
```py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
```
