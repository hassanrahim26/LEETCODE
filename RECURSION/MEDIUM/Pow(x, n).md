## [Pow(x, n)](https://leetcode.com/problems/powx-n/)

* **C++**
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        if(n == 0)
            return 1;
        double y = myPow(x, n/2);
        if(n % 2 == 0)
        {
            return y * y;
        }
        else
        {
            return n < 0 ? 1/x*y*y : x*y*y;
        }
    }
};
```

* **Python**
```py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n, x = -n, 1/x
        
        y = self.myPow(x, n//2)
        return x * y * y if n % 2 else y * y
```
