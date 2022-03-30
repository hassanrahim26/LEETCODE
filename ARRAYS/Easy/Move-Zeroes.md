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

