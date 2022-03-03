## [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)

* **C++**
```cpp
class Solution {
public:
    int xorOperation(int n, int start) {
        int x = start;
        for(int i = 1; i < n; i++)
        {
            x = x ^ (start + 2*i);
        }
        return x;
    }
};
```

* **Python**
```py
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = start
        for i in range(1, n):
            x = x ^ (start + 2*i)
        return x
```
