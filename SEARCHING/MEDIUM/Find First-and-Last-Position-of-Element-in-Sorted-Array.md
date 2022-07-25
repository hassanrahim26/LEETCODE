## [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

* **C++**
```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int a = binarySearch(nums, target);
        int b = binarySearch(nums, target+1)-1;
        if(a < nums.size() and nums[a] == target)
            return {a, b};
        return {-1, -1};
    }
    
    int binarySearch(vector<int>& nums, int target){
        int low = 0, high = nums.size()-1;
        while(low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] < target)
                low = mid + 1;
            else
                high = mid-1;
        }
        return low;
    }
};
```

* **PYTHON**
```py
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = self.binarySearch(nums, target)
        b = self.binarySearch(nums, target+1)-1
        if a < len(nums) and nums[a] == target:
            return [a, b]
        return [-1, -1]
        
    def binarySearch(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid-1
        return low
```
