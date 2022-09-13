## [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

* **C++**
```cpp
class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int c = 0;
        for(auto& x: data){
            if(c == 0){
                if((x >> 5) == 0b110)
                    c = 1;
                else if((x >> 4) == 0b1110)
                    c = 2;
                else if((x >> 3) == 0b11110)
                    c = 3;
                else if((x >> 7) != 0)
                    return false;
            }
            else{
                if((x >> 6) != 0b10)
                    return false;
                else
                    c--;
            }
        }
        return c == 0;
    }
};
```

* **PYTHON**
```py
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        c = 0
        for x in data:
            if c == 0:
                if (x >> 5) == 0b110:
                    c = 1
                elif ((x >> 4) == 0b1110):
                    c = 2
                elif ((x >> 3) == 0b11110):
                    c = 3
                elif ((x >> 7) != 0):
                    return False
            else:
                if (x >> 6) != 0b10:
                    return False
                else:
                    c -= 1
        return c == 0
```
