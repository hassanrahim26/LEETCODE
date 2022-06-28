## [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

* **C++**
```cpp
class Solution {
public:
    int minDeletions(string s) {
        vector<int> v(26, 0);
        for(char c: s)
            v[c - 'a']++;
        
        sort(v.begin(), v.end());
        int ans = 0;
        
        for(int i = 24; i >= 0 and v[i] > 0; i--)
        {
            if(v[i] >= v[i+1])
            {
                int prev = v[i];
                v[i] = max(0, v[i+1] - 1);
                ans += prev - v[i];
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def minDeletions(self, s: str) -> int:
        v = [0]*26
        
        for c in s:
            v[ord(c) - ord('a')] += 1
        
        v.sort(reverse = True)
        ans , x = 0, v[0] - 1
        
        for i in v[1:]:
            if i > x:
                ans += i - x
                i = x
            x = max(0, i - 1)
        
        return ans
```
