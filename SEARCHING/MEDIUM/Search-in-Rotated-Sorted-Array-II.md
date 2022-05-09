## [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

* **C++**
```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        
        while(low <= high){
            int mid = low + (high - low)/2;
            
            if(nums[mid] == target)
                return true;
            
            if(nums[low] == nums[mid] and nums[high] == nums[mid])
            {
                low++;
                high--;
            }
            
            else if(nums[low] <= nums[mid])
            {
                if(target < nums[mid] and target >= nums[low])
                    high = mid - 1;
                else
                    low = mid + 1;
            }
            
            else
            {
                if(target > nums[mid] and target <= nums[high])
                    low = mid + 1;
                else
                    high = mid - 1;
            }
        }
        
        return false;
    }
};
```

* **Python**
```py
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                return True
            
            if nums[low] == nums[mid] and nums[high] == nums[mid]:
                low += 1
                high -= 1
            
            elif nums[low] <= nums[mid]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
```
