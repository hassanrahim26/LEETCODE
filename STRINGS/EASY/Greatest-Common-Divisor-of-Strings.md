## [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

* **C++**
```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        return (str1 + str2 == str2 + str1) ? str1.substr(0, gcd(str1.length(), str2.length())) : "";
    }
};
```
* **Python**
```py
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:math.gcd(len(str1), len(str2))] if str1 + str2 ==  str2 + str1 else ''        
```
