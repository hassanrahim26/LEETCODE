## [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

* **C++**
```cpp
class Solution {
public:
    bool hasAllCodes(string s, int k) {
        if(k > s.size())    
            return false;
        unordered_set<string> mp;
        
        for(int i = 0; i <= s.size() - k; i++)
            mp.insert(s.substr(i, k));
        
        return mp.size() == pow(2, k);
    }
};
```

* **Python**
```py
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        for i in range(k, len(s) + 1):
            st.add(s[i - k : i])
            if len(st) == 1 << k:
                break
        
        return len(st) == 1 << k
```
