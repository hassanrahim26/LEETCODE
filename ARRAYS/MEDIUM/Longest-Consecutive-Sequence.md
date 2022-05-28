## [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

* **C++**
```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int ans = 0, count;
        
        for(auto n: numSet){
            if(!numSet.count(n-1)){
                count = 0;
                while(numSet.count(n)){
                    count++;
                    n += 1;
                }
                ans = max(ans, count);
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        
        for n in nums:
            if n - 1 not in nums:
                left, right = n, n
                while right + 1 in nums:
                    right += 1
                ans = max(ans, right - left + 1)
        
        return ans
```
