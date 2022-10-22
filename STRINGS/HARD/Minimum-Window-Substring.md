## [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

* **C++**
```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> mp(128, 0);
        for(auto c: t){
            mp[c]++;
        }
        int low = 0, high = 0, m = s.size(), n = t.size(), minStart = 0, minLen = INT_MAX;
        
        while(high < m){
            if(mp[s[high]] > 0)
                n--;
            mp[s[high]]--;
            high++;
            
            while(n == 0){
                if(high - low < minLen){
                    minStart = low;
                    minLen = high - low;
                }
                mp[s[low]]++;
                if(mp[s[low]] > 0)
                    n++;
                low++;
            }
        }
        if(minLen != INT_MAX)
            return s.substr(minStart, minLen);
        return "";
    }
};
```
