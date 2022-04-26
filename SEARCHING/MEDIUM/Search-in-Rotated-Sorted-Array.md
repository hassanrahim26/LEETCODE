## [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

* **C++**
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0, high = nums.size()-1, mid;
        
        while(low <= high){
            mid = low + (high - low)/2;
            
            if(nums[mid] == target)
                return mid;
            
            if(nums[low] <= nums[mid])
            {
                if(target <= nums[mid] and target >= nums[low])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
            
            else
            {
                if(target >= nums[mid] and target <= nums[high])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
        }
        
        return -1;
    }
};
```

* **Python**
```py
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2
            
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
```
