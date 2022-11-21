## [Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

* **C++**
```cpp
class Solution {
public:
    int nearestExit(vector<vector<char>>& m, vector<int>& e) {
        queue<pair<int, int>> q;
        q.push({e[0], e[1]});
        
        int moves = 1, r = m.size(), c = m[0].size();
        vector<vector<int>> v = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        m[e[0]][e[1]] = '+';
        
        while(!q.empty()){
            int l = q.size();
            for(int k = 0; k < l; k++){
                auto [i, j] = q.front();
                q.pop();
                
                for(int l = 0; l < 4; l++){
                    int x = i + v[l][0];
                    int y = j + v[l][1];
                    
                    if(x < 0 || y < 0 || x >= r || y >= c || m[x][y] == '+')
                        continue;
                    if(x == 0 || y == 0 || x == r-1 || y == c-1)
                        return moves;
                    
                    m[x][y] = '+';
                    q.push({x, y});
                }
            }
            moves++;
        }
        return -1;
    }
};
```
