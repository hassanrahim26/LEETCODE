## [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

* **C++**
```cpp
class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<bool> vis(n, false);
        queue<int> q;
        q.push(0);
        vis[0] = true;
        
        while(!q.empty()){
            int room = q.front();
            q.pop();
            for(auto it: rooms[room]){
                if(!vis[it]){
                    q.push(it);
                    vis[it] = true;
                }
            }
        }
        for(auto it: vis)
            if(!it)
                return false;
        return true;
    }
};
```
