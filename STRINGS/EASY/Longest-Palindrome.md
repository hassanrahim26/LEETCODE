## [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

* **C++**
```cpp
class Solution {
public:
    int longestPalindrome(string s) {
        int mp[128] = {};
        for(auto c: s)
            mp[c]++;
        
        int x = 0;
        for(auto i: mp)
            x += i & 1;
        
        return s.size() - x + (x > 0);
    }
};
```

* **Python**
```py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = [0]*128
        for c in s:
            mp[ord(c)] += 1
        
        odd = 0
        for i in mp:
            odd += i & 1
        
        return len(s) - odd + (odd > 0)
```
