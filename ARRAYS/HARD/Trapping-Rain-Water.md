## [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

* **C++**
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() == 0)
            return 0;
        int l = 0, r = height.size() - 1, ans = 0;
        int leftMax = height[l], rightMax = height[r];
        
        while(l < r){
            if(leftMax < rightMax){
                l += 1;
                leftMax = max(leftMax, height[l]);
                ans += leftMax - height[l];
            }
            else{
                r -= 1;
                rightMax = max(rightMax, height[r]);
                ans += rightMax - height[r];
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        
        return res
        
```
