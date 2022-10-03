## [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/)

* **C++**
```cpp
class Solution {
public:
    int minCost(string s, vector<int>& v) {
        int cost = 0;
        for(int i = 1; i < v.size(); i++){
            if(s[i] == s[i-1]){
                cost += min(v[i], v[i-1]);
                v[i] = max(v[i], v[i-1]);
            }
        }
        return cost;
    }
};
```

* **PYTHON**
```py
class Solution:
    def minCost(self, s: str, v: List[int]) -> int:
        cost = 0
        for i in range(1, len(v)):
            if(s[i] == s[i-1]):
                cost += min(v[i], v[i-1])
                v[i] = max(v[i], v[i-1])
        return cost
```
