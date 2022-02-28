## [Is Subsequence](https://leetcode.com/problems/is-subsequence/)

* **C++**
```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int n = s.size(), m = t.size();
        int i = 0, j = 0;
        while(i < n && j < m)
        {
            if(s[i] == t[j])
            {
                i++;
            }
            j++;
        }
        return i == n ? 1 : 0;
    }
};
```

* **Python**
```py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i, j = 0, 0
        while(i < n and j < m):
            if s[i] == t[j]:
                i += 1
            j += 1
        return 1 if i == n else 0
        
```
