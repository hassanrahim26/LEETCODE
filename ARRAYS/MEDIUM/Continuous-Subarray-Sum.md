## [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

* **C++**
```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int cur = 0;
        unordered_map<int, int> mp = {{0, -1}};
        for(int i = 0; i < nums.size(); i++){
            if(k)
                cur = (cur + nums[i]) % abs(k);
            else
                cur + nums[i];
            mp.insert({cur, i});
            if(i - mp[cur] > 1)
                return true;
        }
        return false;
    }
};
```

* **PYTHON**
```py
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cur = 0
        mp = {0: -1}
        
        for i in range(len(nums)):
            if(k):
                cur = (cur + nums[i]) % abs(k)
            else:
                cur += nums[i]
            if cur not in mp:
                mp[cur] = i
            if(i - mp[cur] > 1):
                return True
        return False
```
