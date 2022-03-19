## [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i = 0; i < numRows; i++)
        {
            vector<int> row(i+1, 1);
            for(int j = 1; j < i; j++)
            {
                row[j] = ans[i-1][j] + ans[i-1][j-1];
            }
            ans.push_back(row);
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [0]*numRows
        for i in range(numRows):
            ans[i] = [0]*(i+1)
            ans[i][0] = 1
            ans[i][i] = 1
            for j in range(1, i):
                ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        return ans
```
