## [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

* **C++**
```cpp
class Solution {
    bool valid(string s, int i, int j)
    {
        while(i < j)
        {
            if(s[i] != s[j])
                return false;
            i++;
            j--;
        }
        return true;
    }
    
public:
    bool validPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        
        while(i < j)
        {
            if(s[i] != s[j])
                return valid(s, i, j-1) || valid(s, i+1, j);
            i++;
            j--;
        }
        
        return true;
    }
};
```

* **Python**
```py
class Solution:
    def valid(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return self.valid(s, i, j-1) or self.valid(s, i+1, j)
            i += 1
            j -= 1
        return True
```
