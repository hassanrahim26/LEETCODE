## [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

* **C++**
```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        sort(nums.begin(), nums.end());
        int mid = nums[n/2];
        for(int x: nums)
            ans += abs(x - mid);
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        mid = nums[n//2]
        for x in nums:
            ans += abs(x - mid)
        return ans
```
