## [Candy](https://leetcode.com/problems/candy/)

* **C++**
```cpp
class Solution {
public:
    int candy(vector<int>& r) {
        int n = r.size();
        vector<int> ans(n, 1);
        
        for(int i = 0; i < n - 1; i++)
            if(r[i] < r[i+1])
                ans[i+1] = max(1+ans[i], ans[i+1]);
        
        for(int i = n - 2; i >= 0; i--)
            if(r[i+1] < r[i])
                ans[i] = max(1+ans[i+1], ans[i]);
        
        int sum = 0;
        for(auto x: ans)
            sum += x;
    
        return sum;
    }
};
```

* **Python**
```py
class Solution:
    def candy(self, r: List[int]) -> int:
        n, ans = len(r), [1]*len(r)
        
        for i in range(n-1):
            if r[i] < r[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
        
        for i in range(n-2, -1, -1):
            if r[i+1] < r[i]:
                ans[i] = max(1 + ans[i+1], ans[i])
        
        return sum(ans)
```
