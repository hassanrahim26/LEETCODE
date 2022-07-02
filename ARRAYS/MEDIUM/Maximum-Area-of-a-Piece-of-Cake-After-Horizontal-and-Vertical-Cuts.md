## [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

* **C++**
```cpp
class Solution {
public:
    int maxArea(int h, int w, vector<int>& hc, vector<int>& vc) {
        hc.push_back(h);
        vc.push_back(w);
        sort(hc.begin(), hc.end());
        sort(vc.begin(), vc.end());
        int d1 = hc[0], d2 = vc[0];
        
        for(int i = 1; i < hc.size(); i++)
            d1 = max(d1, hc[i] - hc[i-1]);
        
        for(int i = 1; i < vc.size(); i++)
            d2 = max(d2, vc[i] - vc[i-1]);
        
        return (1LL * d1 * d2) % (1000000007);
    }
};
```

* **Python**
```py
class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.append(h)
        vc.append(w)
        hc.sort()
        vc.sort()
        d1, d2 = hc[0], vc[0]
        
        for i in range(1, len(hc)):
            d1 = max(d1, hc[i] - hc[i-1])
        
        for i in range(1, len(vc)):
            d2 = max(d2, vc[i] - vc[i-1])
            
        return (d1 * d2) % 1000000007
```
