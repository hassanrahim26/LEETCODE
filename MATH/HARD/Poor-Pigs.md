## [Poor Pigs](https://leetcode.com/problems/poor-pigs/)

* **C++**
```cpp
class Solution {
public:
    int poorPigs(int b, int m1, int m2) {
        return ceil(log(b)/log(m2/m1 +1));
    }
};
```

* **PYTHON**
```py
class Solution:
    def poorPigs(self, b: int, m1: int, m2: int) -> int:
        return ceil(log(b)/log(m2/m1 +1))        
```
