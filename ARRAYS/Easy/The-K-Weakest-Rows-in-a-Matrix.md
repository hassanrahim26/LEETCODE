## [The K Weakest Rows in a Matrix](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/)

* **C++**
```cpp
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int n = mat[0].size();
        
        for(int i = 0; i < mat.size(); i++)
        {
            mat[i].push_back(i);
        }
        
        sort(mat.begin(), mat.end());
        vector<int> ans(k);
        
        for(int i = 0; i < k; i++)
        {
            ans[i] = mat[i][n];
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        
        for i, n in enumerate(mat):
            ans.append([sum(n), i])
        ans.sort()
        
        return [k for j, k in ans[0:k]]
```
