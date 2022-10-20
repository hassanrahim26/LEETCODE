## [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

* **C++**
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        ans[n-1] = 1;
        for(int i = n-2; i >= 0; i--){
            ans[i] = nums[i+1] * ans[i+1];
        }
        int leftProd = 1;
        for(int i = 0; i < n; i++){
            ans[i] *= leftProd;
            leftProd *= nums[i];
        }
        return ans;
    }
};
```

* **PYTHON**
```py
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        ans[n-1] = 1
        
        for i in range(n-2, -1, -1):
            ans[i] = nums[i+1] * ans[i+1]
        
        leftProd = 1
        for i in range(0, n):
            ans[i] *= leftProd
            leftProd *= nums[i]
        
        return ans
```
