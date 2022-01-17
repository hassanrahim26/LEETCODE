## [Rotate Array](https://leetcode.com/problems/rotate-array/)

* **C++**
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> ans = nums;
        int n = nums.size();
        k = n - k % n;
        
        for(int i = 0; i < n; i++)
            nums[i] = ans[(i + k) % n];
    }
};
```

* **Python**
```py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```
