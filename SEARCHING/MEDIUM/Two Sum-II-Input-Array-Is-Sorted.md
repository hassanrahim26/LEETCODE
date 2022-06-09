## [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

* **C++**
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int low = 0, high = nums.size() - 1;
        
        while(low < high){
            
            if(nums[low] + nums[high] == target)
                return {low + 1, high + 1};
            
            else if(nums[low] + nums[high] > target)
                high--;
            
            else
                low++;
        }
        
        return {};
    }
};
```

* **Python**
```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        
        while low < high:
            s = nums[low] + nums[high]
            
            if s == target:
                return [low + 1, high + 1]
            elif s > target:
                high -= 1
            else:
                low += 1
        return []
```
