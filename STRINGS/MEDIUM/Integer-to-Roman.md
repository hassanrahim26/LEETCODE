## [Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

* **C++**
```cpp
class Solution {
public:
    string intToRoman(int num) {
        string ans;
        string c[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        
        for(int i = 0; num != 0; i++)
        {
            while(num >= val[i])
            {
                num -= val[i];
                ans += c[i];
            }
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        c = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ans = ""
        for i in range(13):
            while num >= val[i]:
                num -= val[i]
                ans += c[i]
        return ans
        
```
