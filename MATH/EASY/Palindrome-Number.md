## [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

* **C++**
```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0 || (x != 0 && x % 10 == 0))
            return false;
        
        int rev = 0;
        while(rev < x)
        {
            rev = rev * 10 + x % 10;
            x /= 10;
        }
        
        return x == rev || x == rev/10;
    }
};
```
