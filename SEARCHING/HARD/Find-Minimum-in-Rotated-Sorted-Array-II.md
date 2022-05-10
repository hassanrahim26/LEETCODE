## [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

* **C++**
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        
        while(low < high){
            int mid = low + (high - low)/2;
            
            if(nums[mid] < nums[high])
                high = mid;
            else if(nums[mid] == nums[high])
                high--;
            else
                low = mid + 1;
        }
        
        return nums[low];
    }
};
```

* **Python**
```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low)//2
            
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                low = mid + 1
        
        return nums[low]
```
