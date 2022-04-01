## [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

* **C++**
```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        
        while(left < right)
        {
            int mid = left + (right-left)/2;
            
            if(nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }
        
        return nums[left];
    }
};
```

* **Python**
```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```
