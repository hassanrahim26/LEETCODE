## [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)

* **C++**
```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& box, int t) {
        sort(box.begin(), box.end(), [](auto &a, auto &b) {
            return b[1] < a[1];
        });
        int ans = 0;
        
        for(auto& b: box)
        {
            int count = min(b[0], t);
            ans += count * b[1];
            t -= count;
            if(!t)
                return ans;
        }
       
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def maximumUnits(self, box: List[List[int]], t: int) -> int:
        box.sort(key=lambda x: x[1], reverse = True)
        ans = 0
        
        for b, n in box:
            count = min(b, t)
            ans += count * n
            t -= count
            if not t:
                return ans
            
        return ans
```
