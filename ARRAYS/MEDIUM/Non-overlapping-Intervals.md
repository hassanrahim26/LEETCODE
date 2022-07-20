## [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

* **C++**
```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& v) {
        sort(v.begin(), v.end());
        int c = 0, l = 0, r = 1, n = v.size();
        
        while(r < n)
        {
            if(v[l][1] <= v[r][0]){
                l = r;
                r++;
            }
            else if(v[l][1] <= v[r][1]){
                c++;
                r++;
            }
            else if(v[l][1] > v[r][1]){
                c++;
                l = r;
                r++;
            }
        }
        return c;
    }
};
```

* **Python**
```py
class Solution:
    def eraseOverlapIntervals(self, v: List[List[int]]) -> int:
        v.sort()
        c, l, r, n = 0, 0, 1, len(v)
        
        while(r < n):
            if v[l][1] <= v[r][0]:
                l = r
                r += 1
            elif v[l][1] <= v[r][1]:
                c += 1
                r += 1
            elif v[l][1] > v[r][1]:
                c += 1
                l = r
                r += 1
        return c
            
```
