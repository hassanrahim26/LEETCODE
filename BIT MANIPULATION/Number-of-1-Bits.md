## [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

* **C++**
```cpp
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int c = 0;
        while(n)
        {
            n &= (n-1);
            c++;
        }
        return c;
    }
};
```

* **Python**
```py
class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= (n-1)
            c += 1
        return c
```
