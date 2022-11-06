## [Orderly Queue](https://leetcode.com/problems/orderly-queue/)

* **C++**
```cpp
class Solution {
public:
    string orderlyQueue(string s, int k) {
        if(k > 1){
            sort(s.begin(), s.end());
            return s;
        }
        string ans = s;
        for(int i = 1; i < s.length(); i++){
            ans = min(ans, s.substr(i) + s.substr(0, i));
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1: return "".join(sorted(s))
        return min(s[i:] + s[:i] for i in range(len(s)))
```
