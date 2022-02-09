## [Power of Three](https://leetcode.com/problems/power-of-three/)

* **C++**
```cpp
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n == 0)    
            return false;
        while(n% 3 == 0)
            n /= 3;
        return n == 1;
    }
};
```

* **Python**
```py
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        while(n%3 == 0):
            n /= 3
        return n == 1
        
```
