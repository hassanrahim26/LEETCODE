## [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

* **C++**
```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& v) {
        int n = v.size();
        vector<bool>check(n+1, false);
        
        for(int i = 0; i < n; i++)
            if(v[i] > 0 and v[i] <= n)
                check[v[i]] = true;
        
        for(int i = 1; i <= n; i++)
            if(!check[i])
                return i;
        
        return n+1;
    }
};
```

* **PYTHON**
```py
class Solution:
    def firstMissingPositive(self, v: List[int]) -> int:
        n = len(v)
        check = [False]*(n+1)
        
        for i in range(n):
            if v[i] > 0 and v[i] <= n:
                check[v[i]] = True
        
        for i in range(1, n+1):
            if not check[i]:
                return i
        
        return n+1
```
