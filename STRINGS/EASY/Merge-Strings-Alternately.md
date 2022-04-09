## [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

* **C++**
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n = max(word1.size(), word2.size());
        string ans = "";
        
        for(int i = 0; i < n; i++)
        {
            if(word1.size() > i)
                ans += word1[i];
            if(word2.size() > i)
                ans += word2[i];
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        n = max(len(word1), len(word2))
        
        for i in range(n):
            if len(word1) > i:
                ans += word1[i]
            if len(word2) > i:
                ans += word2[i]
                
        return ans
```
