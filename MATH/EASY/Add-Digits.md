## [Add Digits](https://leetcode.com/problems/add-digits/)

* **C++**
```cpp
class Solution {
public:
    int addDigits(int num) {
        if(num == 0)
            return 0;
        else if(num % 9 == 0)
            return 9;
        else 
            return num % 9;
    }
};
```

* **Python**
```py
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
```
