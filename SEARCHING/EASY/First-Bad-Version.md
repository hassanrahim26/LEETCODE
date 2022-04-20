## [First Bad Version](https://leetcode.com/problems/first-bad-version/)

* **C++**
```cpp
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1, high = n, mid;
        
        while(low < high){
            mid = low + (high - low)/2;
            
            if(!isBadVersion(mid))
                low = mid + 1;
            else
                high = mid;
        }
        
        return low;
    }
};
```

* **Python**
```py
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        
        while low < high:
            mid = low + (high - low)//2
            
            if not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid
            
        return low
```
