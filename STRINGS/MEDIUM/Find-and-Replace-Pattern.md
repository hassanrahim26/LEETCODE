## [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

* **C++**
```cpp
class Solution {
public:
    string solve(string w) {
	    unordered_map<char, char> mp;
	    char c = 'a';
	    for(auto ch : w) 
		    if(!mp.count(ch)) mp[ch] = c++;
    	for(auto& ch : w) ch = mp[ch];
        	return w;
    }
    
    vector<string> findAndReplacePattern(vector<string>& words, string p) {
        vector<string> ans;
        for(string& w: words)
            if(solve(w) == solve(p))
                ans.push_back(w);
        return ans;
    }
};
```
