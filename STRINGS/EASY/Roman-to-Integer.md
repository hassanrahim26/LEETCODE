## [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

* **C++**
```cpp
class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp = {{'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1}};
        
        int ans = mp[s.back()];
        
        for(int i = 0; i < s.size() - 1; i++)
        {
            if(mp[s[i]] < mp[s[i+1]])
                ans -= mp[s[i]];
            else
                ans += mp[s[i]];
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        ans = mp[s[-1]]
        
        for i in range(0, len(s)-1):
            if mp[s[i]] < mp[s[i+1]]:
                ans -= mp[s[i]]
            else:
                ans += mp[s[i]]
        
        return ans
```
