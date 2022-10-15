## [Multiply Strings](https://leetcode.com/problems/multiply-strings/)

* **C++**
```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0")
            return "0";
        string ans(size(num1) + size(num2), '0');
        
        for(int i = size(num1) - 1; i >= 0; i--){
            for(int j = size(num2) - 1; j >= 0; j--){
                int res = (ans[i+j+1] - '0') + (num1[i] - '0') * (num2[j] - '0');
                ans[i+j+1] = res%10 + '0';
                ans[i+j] += res/10;
            }
        }
        
        if(ans[0] == '0')
            return ans.substr(1);
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        def f1(num):
            ans = 0
            for i in num:
                ans = ans*10 +(ord(i) - ord('0'))
            return ans

        def f2(n):
            ans = ''
            while n:
                a = n % 10
                n = n // 10
                ans = chr(ord('0') + a) + ans
            return ans
        
        return f2(f1(num1)*f1(num2))
```
