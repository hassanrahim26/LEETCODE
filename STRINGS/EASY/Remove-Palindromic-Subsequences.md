## [Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/)

* **C++**
```cpp
class Solution {
public:
    int removePalindromeSub(string s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            if(s[i] != s[j])
                return 2;
            i++;
            j--;
        }
        return 1;
    }
};
```

* **Python**
```py
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return 2
            i += 1
            j -= 1
        return 1
```
