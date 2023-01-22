## [Binary Search](https://leetcode.com/problems/binary-search/)

* **C++**
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        while(low <= high)
        {
            int mid = low + (high - low)/2;
            
            if(nums[mid] == target)
            {
                return mid;
            }
            
            else if(target > nums[mid])
            {
                low = mid + 1;
            }
            
            else
            {
                high = mid - 1;
            }
        }
        
        return -1;
    }
};
```

* **PYTHON**
```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int(low + (high - low)/2)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
```
