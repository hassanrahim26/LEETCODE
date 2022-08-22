## [Total Appeal of A String](https://leetcode.com/problems/total-appeal-of-a-string/)

* **C++**
```cpp
class Solution {
public:
    long long appealSum(string s) {
        vector<int> v(26);
        long long ans = 0, n = s.size(), total = 0;    
        for(int i = 0; i < n; i++){
            total += i + 1 - v[s[i] - 'a'];
            v[s[i] - 'a'] = i+1;
            ans += total;
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def appealSum(self, s: str) -> int:
        v = [0]*26
        ans, n, total = 0, len(s), 0
        for i in range(n):
            total += i + 1 - v[ord(s[i]) - ord('a')]
            v[ord(s[i]) - ord('a')] = i+1
            ans += total
        return ans
```
