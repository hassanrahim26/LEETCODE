## [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

* **C++**
```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& v) {
        int n = v.size(), m = v[0].size();
        set<int> rows, cols;
        
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(v[i][j] == 0){
                    rows.insert(i);
                    cols.insert(j);
            }
    
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(rows.count(i) || cols.count(j))
                    v[i][j] = 0;   
    }
};
```

* **Python**
```py
class Solution:
    def setZeroes(self, v: List[List[int]]) -> None:
        n, m = len(v), len(v[0])
        rows, cols = set(), set()
        
        for i in range(n):
            for j in range(m):
                if v[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    v[i][j] = 0
```
