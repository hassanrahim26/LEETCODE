## [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/)

* **C++**
```cpp
class Solution {
public:
    bool judgeSquareSum(int c) {
        if(c < 3)
            return true;
        
        long long int a = 0, b = sqrt(c);
        
        while(a <= b)
        {
            if(a * a + b * b == c)
                return true;
            else if(a * a + b * b < c)
                a++;
            else
                b--;
        }
        
        return false;
    }
};
```

* **Python**
```py
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        a, b = 0, int(math.sqrt(c))
        
        while a <= b:
            if a * a + b *b == c:
                return True
            elif a * a + b * b < c:
                a += 1
            else:
                b -= 1
        
        return False
```
