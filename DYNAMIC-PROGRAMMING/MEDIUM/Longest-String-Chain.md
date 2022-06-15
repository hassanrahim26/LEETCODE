## [Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

* **C++**
```cpp
class Solution {
    static bool compare(string &s1, string &s2){
        return s1.length() < s2.length();
    }
    
public:
    int longestStrChain(vector<string>& words) {
        int res = 0;
        sort(words.begin(), words.end(), compare);
        unordered_map<string, int> dp;
        
        for(string w: words){
            for(int i = 0; i < w.length(); i++){
                string s = w.substr(0, i) + w.substr(i+1);
                dp[w] = max(dp[w], dp.find(s) == dp.end() ? 1 : dp[s] + 1);
            }
            
            res = max(res, dp[w]);
        }
        
        return res;
    }
};
```
