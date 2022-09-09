## [The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)

* **C++**
```cpp
class Solution {
public:
    static bool compare(vector<int>& a, vector<int>& b){
        if(a[0] == b[0])
            return a[1] < b[1];
        return a[0] > b[0];
    }
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        int ans = 0, cmax = INT_MIN;
        sort(properties.begin(), properties.end(), compare);
        for(auto p: properties){
            if(cmax > p[1])
                ans++;
            else
                cmax = p[1];
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0],x[1]))
        ans, cmax = 0, 0
        
        for p in properties:
            if cmax > p[1]:
                ans += 1
            else:
                cmax = p[1]
        return ans
```
