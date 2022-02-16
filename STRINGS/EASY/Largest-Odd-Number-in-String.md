## [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/)

* **C++**
```cpp
class Solution {
public:
    string largestOddNumber(string num) 
    {
        int n=num.size();
        if((num[n-1]-'0')%2==1)
        {
            return num;
        }
        while(num.size()!=0&&(num.back()-'0')%2==0)
        {
            num.pop_back();
        }
        return num;
    }
};
```

* **Python"
```py
class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0:
            if int(num[i])%2:
                return num[:i+1]
            i -= 1
        return ""
```
