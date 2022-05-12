## [Permutations II](https://leetcode.com/problems/permutations-ii/)

* **C++**
```cpp
class Solution {
public:
    vector<vector<int>> ans;
    
    void helper(vector<int> nums, int idx){
        if(idx == nums.size())    
            ans.push_back(nums);
    
        for(int i = idx; i < nums.size(); i++){
            if(i != idx and nums[i] == nums[idx])
                continue;
            swap(nums[i], nums[idx]);
            helper(nums, idx + 1);
        }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        helper(nums, 0);
        return ans;
    }
};
```
