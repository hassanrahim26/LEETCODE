## [Ransom Note](https://leetcode.com/problems/ransom-note/)

* **C++**
```cpp
class Solution {
public:
    bool canConstruct(string r, string m) {
        int mp[26] = {0};
        for(char c: m)
            mp[c - 'a']++;
        for(char c: r){
            if(mp[c - 'a']-- <= 0)
                return false;
        }
        return true;
    }
};
```

* **PYTHON**
```py
class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        return collections.Counter(r) <= collections.Counter(m)
```
