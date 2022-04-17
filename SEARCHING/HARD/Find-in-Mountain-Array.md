## [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

* **C++**
```cpp
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length(), peak = 0, low = 0, high = n-1;
        
        while(low < high)
        {
            int mid = low + (high - low)/2;
            
            if(mountainArr.get(mid)<mountainArr.get(mid+1))
                low = mid + 1;
            else
                high = mid;
        }
        
        peak = low;
        low = 0, high = peak;
        
        while(low <= high)
        {
            int mid = low + (high - low)/2;
            
            if(mountainArr.get(mid) < target)
                low = mid + 1;
            else if(mountainArr.get(mid) == target)
                return mid;
            else
                high = mid-1;
        }
        
        low = peak + 1, high = n-1;
        
        while(low <= high)
        {
            int mid = low + (high - low)/2;
            
            if(mountainArr.get(mid) > target)
                low = mid+1;
            else if(mountainArr.get(mid) == target)
                return mid;
            else
                high = mid-1;
        }
        return -1;
    }
};
```

* **Python**
```py
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        peak, low, high = 0, 0 , n - 1
        
        while low < high:
            mid = low + (high - low)//2
            
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                low = mid + 1
            else:
                high = mid
            
        peak = low
        low, high = 0, peak
        
        while low <= high:
            mid = low + (high - low)//2
            
            if mountain_arr.get(mid) < target:
                low = mid + 1
            elif mountain_arr.get(mid) == target:
                return mid
            else:
                high = mid - 1;
            
        low, high = peak + 1, n - 1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if mountain_arr.get(mid) > target:
                low = mid + 1
            
            elif mountain_arr.get(mid) == target:
                return mid
            else:
                high = mid - 1
        
        return -1
```
