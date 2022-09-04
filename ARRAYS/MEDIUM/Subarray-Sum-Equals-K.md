## [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

* **C++**
```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int c = 0, sum = 0;
        unordered_map<int, int> mp;
        mp[0] = 1;
        
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            c += mp[sum - k];
            mp[sum]++;
        }
        return c;
    }
};
```

* **PYTHON**
```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = collections.Counter()
        mp[0] = 1
        c, s = 0, 0
        
        for x in nums:
            s += x
            c += mp[s-k]
            mp[s] += 1
        return c
```
