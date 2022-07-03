## [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

* **C++**
```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int a = 1, b = 1;
        for(int i = 1; i < nums.size(); i++)
        {
            if(nums[i] > nums[i-1])
                a = b + 1;
            else if(nums[i] < nums[i-1])
                b = a + 1;
        }
        return max(a, b);
    }
};
```

* **Python**
```py
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        a, b = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                a = b + 1
            elif nums[i] < nums[i-1]:
                b = a + 1
        return max(a, b)
```
