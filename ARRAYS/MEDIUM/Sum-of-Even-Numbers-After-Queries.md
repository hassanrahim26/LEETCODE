## [Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)

* **C++**
```cpp
class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> ans;
        int s = 0;
        for(auto x: nums){
            if(x%2 == 0){
                s += x;
            }
        }
        for(auto q: queries){
            int val = q[0], idx = q[1];
            if(nums[idx] % 2 == 0)
                s -= nums[idx];
            nums[idx] += val;
            if(nums[idx] % 2 == 0)
                s += nums[idx];
            ans.push_back(s);
        }
        return ans;
    }   
};
```

* **PYTHON**
```py
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = 0
        for x in nums:
            if x % 2 == 0:
                s += x
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                s -= nums[idx]
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                s += nums[idx]
            ans.append(s)
        
        return ans
```
