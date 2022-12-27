## [Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)

* **C++**
```cpp
class Solution {
public:
    int maximumBags(vector<int>& c, vector<int>& r, int a){
        for(int i = 0; i < c.size(); i++){
            r[i] = (abs(c[i] - r[i]));
        }
        long long s = 0, ans = 0;
        sort(r.begin(), r.end());
        for(auto x: r){
            s += x;
            if(s > a) break;
            else ans++;
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def maximumBags(self, c: List[int], r: List[int], a: int) -> int:
        for i in range(len(c)):
            r[i] = abs(c[i] - r[i])
        s, ans = 0, 0
        r.sort()
        
        for x in r:
            s += x
            if(s > a): break
            else: ans += 1
        return ans
```
