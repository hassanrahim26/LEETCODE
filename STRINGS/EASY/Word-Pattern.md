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

* **PYTHON**
```py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = defaultdict()
        words = s.split(' ')
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): return False
        
        for i, c in enumerate(pattern):
            if c in dic:
                if dic[c] != words[i]: return False
            else:
                dic[c] = words[i]
        return True
```
