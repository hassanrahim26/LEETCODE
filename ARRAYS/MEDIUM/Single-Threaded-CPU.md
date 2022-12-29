## [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/)

* **C++**
```cpp
class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        vector<vector<int>> v;
        for(int i = 0; i < tasks.size(); i++)
            v.push_back({tasks[i][0], tasks[i][1], i});
        sort(v.begin(), v.end());
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; 
        
        long long cur = v[0][0];
        vector<int> ans;
        int i = 0, n = tasks.size();
        
        while(i < n || !pq.empty()){
            while(i < n and cur >= v[i][0]){
                pq.push({v[i][1], v[i][2]});
                i++;
            }
        
            auto p = pq.top();
            cur += p.first;
            ans.push_back(p.second);
            pq.pop();
            
            if(i < n and pq.empty() and cur < v[i][0])
                cur = v[i][0];
        }
        return ans;
    }
};
```
