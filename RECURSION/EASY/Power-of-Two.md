## [Power of Two](https://leetcode.com/problems/power-of-two/)

* **C++**
```cpp
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if(n == 0)
            return false;
        while(n%2 == 0)
            n /= 2;
        return n == 1;
    }
};
```

* **Python**
```py
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return True
        while(n%2 == 0):
            n /= 2
        return n == 1
```
