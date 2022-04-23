## [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

* **C++**
```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), cols = matrix[0].size();
        int n1 = 0, n2 = cols - 1;
			
        while (n1 < rows && n2 > -1) {
            int cur = matrix[n1][n2];
            
            if (cur == target) 
                return true;
            if (target > cur) 
                n1++;
            else
                n2--;
        }
        
        return false;
    }
};
```

* **Python**
```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        n1, n2 = 0, cols - 1;
        
        while n1 < rows and n2 > -1:
            cur = matrix[n1][n2];
            
            if cur == target:
                return True
            elif cur < target:
                n1 += 1
            else:
                n2 -= 1
        
        return False
```
