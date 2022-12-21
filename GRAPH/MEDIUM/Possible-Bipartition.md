## [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)

* **C++**
```cpp
class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<int> color(n+1, 0), visited(n+1, 0);
        visited[0] = 1;
        vector<int> adj[n+1];
        
        for(int i = 0; i < dislikes.size(); i++){
            adj[dislikes[i][0]].push_back(dislikes[i][1]);
            adj[dislikes[i][1]].push_back(dislikes[i][0]);
        }
        
        for(int i = 1; i <= n; i++){
            if(color[i] == 0){
                color[i] = 1;
                queue<int> q;
                q.push(i);
                
                while(!q.empty()){
                    int node = q.front();
                    q.pop();
                    
                    for(auto it: adj[node]){
                        if(color[it] == color[node]) return false;
                        if(!color[it]){
                            q.push(it);
                            color[it] = -1*color[node];
                        }
                    }
                }
            }
        }
        return true;
    }
};
```
