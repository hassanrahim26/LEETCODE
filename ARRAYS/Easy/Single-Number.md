## [Single Number](https://leetcode.com/problems/single-number/)

* **C++**
```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for(auto x: nums)
            ans ^= x;
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
```
