## [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> h;
        for(auto b: buildings){
            h.push_back({b[0], -b[2]});
            h.push_back({b[1], b[2]});
        }
        
        sort(h.begin(), h.end());
        int prev = 0, cur = 0;
        
        multiset<int> m;
        vector<vector<int>> ans;
        
        m.insert(0);
        for(auto i: h){
            if(i.second < 0)
                m.insert(-i.second);
            else
                m.erase(m.find(i.second));
            
            cur = *m.rbegin();
            if(cur != prev){
                ans.push_back({i.first, cur});
                prev = cur;
            }
        }
        return ans;
    }
};
```
