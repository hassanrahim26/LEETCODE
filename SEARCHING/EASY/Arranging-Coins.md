## [Arranging Coins](https://leetcode.com/problems/arranging-coins/)

* **C++**
```cpp
class Solution {
public:
    int arrangeCoins(int n) {
        long low = 0, high = n, mid, temp;
        
        while(low <= high){
            mid = low + (high - low)/2;
            temp = mid * (mid + 1)/2;
            
            if(temp == n)
                return mid;
            
            if(temp <= n)
                low = mid + 1;
            else
                high = mid - 1;
        }
        
        return low-1;
    }
};
```

* **Python**
```py
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        
        while low <= high:
            mid = low + (high - low)//2
            temp = mid * (mid + 1)/2;
            
            if temp == n:
                return mid
            
            if temp <= n:
                low = mid + 1
            else:
                high = mid - 1
        
        return low - 1
            
```
