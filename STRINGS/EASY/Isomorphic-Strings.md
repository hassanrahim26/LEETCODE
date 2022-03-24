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
