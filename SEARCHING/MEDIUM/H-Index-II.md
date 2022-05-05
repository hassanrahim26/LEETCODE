## [H-Index II](https://leetcode.com/problems/h-index-ii/)

* **C++**
```cpp
class Solution {
public:
    int hIndex(vector<int>& c) {
        int n = c.size();
        
        if(!n)
            return 0;
        
        int low = 0, high = n - 1, ans = 0;
        while(low <= high){
            int mid = low + (high - low)/2;
            
            if(c[mid] >= n - mid){
                ans = n - mid;
                high = mid - 1;
            }
            else{
                low = mid + 1;    
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def hIndex(self, c: List[int]) -> int:
        n = len(c)
        
        if not c:
            return 0
        
        low, high, ans = 0, n - 1, 0
        
        while low <= high:
            mid = low + (high - low)//2
            
            if c[mid] >= n - mid:
                ans = n - mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
```
