## [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

* **C++**
```cpp
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int mp1[256] = {0}, mp2[256] = {0}, n = s.size();
        for(int i = 0; i < n; i++)
        {
            if(mp1[s[i]] != mp2[t[i]])
                return false;
            mp1[s[i]] = i+1;
            mp2[t[i]] = i+1;
        }
        return true;
    }
};
```
* **Python**
```py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1, mp2 = {}, {}
        
        for i in range(len(s)):
            if s[i] in mp1 and mp1[s[i]] != t[i]:
                return False
            if t[i] in mp2 and mp2[t[i]] != s[i]:
                return False
            
            mp1[s[i]] = t[i]
            mp2[t[i]] = s[i]
            
        return True
```
