## [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

* **C++**
```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> ans(rowIndex+1, 0);
        ans[0] = 1;
        for(int i = 1; i < rowIndex+1; i++)
            for(int j = i; j >= 1; j--)
                ans[j] += ans[j-1];
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]*(rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                ans[j] += ans[j-1]
        return ans
```
