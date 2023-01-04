## [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)

* **C++**
```cpp
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        int ans = 0;
        int r = strs.size(), c = strs[0].size();
        
        for(int j = 0; j < c; j++){
            for(int i = 0; i < r-1; i++){
                if(strs[i][j] > strs[i+1][j]){
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans, r, c = 0, len(strs), len(strs[0])
        
        for j in range(c):
            for i in range(r-1):
                if(strs[i][j] > strs[i+1][j]):
                    ans += 1
                    break
        
        return ans
```
