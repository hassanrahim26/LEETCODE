## [Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/)

* **C++**
```cpp
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int ans = 0, n = size(matrix), m = size(matrix[0]);
        for(int i = 0; i < n; i++)
            for(int j = 1; j < m; j++)
                matrix[i][j] += matrix[i][j-1];
        
        unordered_map<int, int> mp;
        for(int i = 0; i < m; i++){
            for(int j = i; j < m; j++){
                int s = 0;
                mp = {{0, 1}};
                
                for(int k = 0; k < n; k++){
                    s += matrix[k][j] - (i ? matrix[k][i-1] : 0);
                    ans += mp[s - target];
                    mp[s]++;
                }
            }
        }
        return ans;
    }
};
```
