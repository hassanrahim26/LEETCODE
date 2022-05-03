## [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/)

* **C++**
```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        vector<int> v(nums.begin(), nums.end());
        sort(v.begin(), v.end());
        
        int i = 0, j = nums.size() - 1;
        
        while (i < nums.size() && nums[i] == v[i]) {
            i++;
        }
        
        while (j > i && nums[j] == v[j]) {
            j--;
        }
        
        return j + 1 - i;
    }
};
```

* **Python**
```py
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        v = sorted(nums)
        
        i, j = 0, len(nums) - 1
        
        while i < len(nums) and nums[i] == v[i]:
            i += 1
        
        while j > i and nums[j] == v[j]:
            j -= 1
        
        return j + 1 - i
```
