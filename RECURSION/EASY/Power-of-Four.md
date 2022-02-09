## [Power of Four](https://leetcode.com/problems/power-of-four/)

* **C++**
```cpp
class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n == 0)    
            return false;
        while(n% 4 == 0)
            n /= 4;
        return n == 1;
    }
};
```

* **Python**
```py
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        while(n%4 == 0):
            n /= 4
        return n == 1
        
```
