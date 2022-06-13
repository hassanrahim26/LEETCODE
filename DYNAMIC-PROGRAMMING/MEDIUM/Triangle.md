## [Triangle](https://leetcode.com/problems/triangle/)

* **C++**
```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        for(int i = triangle.size() - 2; i >= 0; i--)
           for(int j = 0; j < i + 1; j++)
               triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]);
        
        return triangle[0][0];
    }
};
```

* **Python**
```py
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(0, i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]
        
```
