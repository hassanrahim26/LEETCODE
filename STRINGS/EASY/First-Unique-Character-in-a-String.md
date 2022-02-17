## [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

* **C++**
```cpp
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> mp;
        for(char &c: s)
        {
            mp[c]++;
        }
        for(int i = 0; i < s.size(); i++)
        {
            if(mp[s[i]] == 1)
                return i;
        }
        
        return -1;
    }
};
```

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in c:
            if c[i] == 1:
                return s.index(i)
        return -1
        
```
