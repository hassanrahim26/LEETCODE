## [Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& matches) {
        vector<int> mp(100001, -1);
        int x = 0;
        for(auto m: matches){
            mp[m[0]] = max(0, mp[m[0]]);
            mp[m[1]] = max(0, mp[m[1]]) + 1;
            x = max(max(x, m[0]), m[1]);
        }
        
        vector<int> v1, v2;
        for(int i = 1; i <= x; i++){
            if(mp[i] == 0) v1.push_back(i);
            if(mp[i] == 1) v2.push_back(i);
        }
        return {v1, v2};
    }
};
```
