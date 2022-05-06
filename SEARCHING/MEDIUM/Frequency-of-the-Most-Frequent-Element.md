## [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/)

* **C++**
```cpp
class Solution {
public:
    int maxFrequency(vector<int>& nums, long k) {
        int i = 0, j;
        sort(nums.begin(), nums.end());
        
        for(j = 0; j < nums.size(); ++j){
            k += nums[j];
            
            if(k < (long)nums[j] * (j - i + 1))
                k -= nums[i++];
        }
        
        return j - i;
    }
};
```

* **Python**
```py
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0;
        nums.sort()
        
        for j in range(len(nums)):
            k += nums[j]
            
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        
        return j - i + 1
```
