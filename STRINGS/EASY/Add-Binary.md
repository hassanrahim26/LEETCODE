## [Add Binary](https://leetcode.com/problems/add-binary/)

* **C++**
```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        string ans;
        int carry = 0;
        
        while(i >= 0 || j >= 0 || carry)
        {
            if(i >= 0)
            {
                carry += a[i] - '0';
                i--;
            }
            
            if(j >= 0)
            {
                carry += b[j] - '0';
                j--;
            }
            
            ans += (carry % 2 + '0');
            carry = carry/2;
        }
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry % 2)
            carry //= 2 
        
        return result[::-1]
```
