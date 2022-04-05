## [Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/)

* **C++**
```cpp
class Solution {
public:
    int arraySign(vector<int>& nums) {
        int ans = 1;
        for(auto x: nums)
        {
            if(x < 0)
                ans *= -1;
            else if(x == 0)
                return 0;
        }
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for x in nums:
            if x < 0:
                ans *= -1
            elif x == 0:
                return 0
        return ans                
```
