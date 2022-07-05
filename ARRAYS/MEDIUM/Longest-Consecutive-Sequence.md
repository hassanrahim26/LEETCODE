## [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

* **C++**
```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());
        int ans = 0, count;
        
        for(auto n: s)
        {
            if(!s.count(n-1))
            {
                count = 0;
                while(s.count(n))
                {
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
        s = set(nums)
        ans = 0
        
        for x in s:
            if x-1 not in s:
                y = x + 1
                while y in s:
                    y += 1
                ans = max(ans, y - x)
        return ans
```
