## [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

* **C++**
```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> mp;
        for(string s: words)
            mp[s]++;
        
        priority_queue<pair<int, string>> pq;
        for(auto it: mp){
            pq.push({-it.second, it.first});
            if(pq.size() > k)
                pq.pop();
        }
        
        vector<string> ans;
        while(k--){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```
