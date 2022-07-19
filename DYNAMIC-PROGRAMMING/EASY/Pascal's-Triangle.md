## [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        for(int i = 0; i < numRows; i++)
        {
            ans.push_back(vector<int>(i+1, 1));
            for(int j = 1; j < i; j++)
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j];
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*(i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans
```
