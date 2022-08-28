## [Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/)

* **C++**

  * 1
    ```cpp
    class Solution {
    public:
        vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
            unordered_map<int, priority_queue<int, vector<int>, greater<int>>> map;
            int n = mat.size(), m = mat[0].size();
        
            for(int i = 0; i < n; i++)
                for(int j = 0; j < m; j++)
                    map[i-j].push(mat[i][j]);
        
            for(int i = 0; i < n; i++){
                for(int j = 0; j < m; j++){
                    mat[i][j] = map[i-j].top();
                    map[i-j].pop();
                }
            }
            return mat;
        }
    };
    ```
    
  * 2
    ```cpp
    class Solution {
    public:
        void solve(vector<vector<int>>& mat, int row, int col){
            vector<int> v;
            int r = row, c = col;
            while(r < mat.size() and c < mat[0].size())
                v.push_back(mat[r++][c++]);
        
            sort(v.begin(), v.end());
            int i = 0;
            while(row < mat.size() and col < mat[0].size())
                mat[row++][col++] = v[i++];
        }
    
        vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
            int n = mat.size(), m = mat[0].size();
        
            for(int i = 0; i < m; i++)
                solve(mat, 0, i);
            for(int i = 1; i < n; i++)
                solve(mat, i, 0);
            return mat;
        }
    };
    ```


