## [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)

* **C++**
```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& m) {
        for(int i = 1; i < m.size(); i++){
            for(int j = 0; j < m[0].size()-1; j++){
                if(m[i-1][j] != m[i][j+1])
                    return false;
            }
        }
        return true;
    }
};
```

* **PYTHON**
```py
class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
        for i in range(1, len(m)):
            for j in range(len(m[0])-1):
                if m[i-1][j] != m[i][j + 1]:
                    return False
        return True
```
