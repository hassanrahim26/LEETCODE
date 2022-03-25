## [Word Pattern](https://leetcode.com/problems/word-pattern/)

* **C++**
```cpp
class Solution {
public:
    bool wordPattern(string p, string s) {
        unordered_map<char, int> mp1;
        unordered_map<string, int> mp2;
        
        stringstream in(s);
        string word;
        
        int i = 0, n = p.size();
        
        for(word; in >> word; i++)
        {
            if(i == n || mp1[p[i]] != mp2[word])
                return false;
            
            mp1[p[i]] = mp2[word] = i + 1;
        }
        
        return i == n;
    }
};
```
