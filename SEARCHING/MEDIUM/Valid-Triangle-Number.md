## [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

* **C++**
```cpp
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        
        for(int i = nums.size() - 1; i >= 0; i--)
        {
            int low = 0, high = i - 1;
            
            while(low < high){
                if(nums[low] + nums[high] > nums[i])
                {
                    ans += high - low;
                    high--;
                }
                else
                    low++;
            }
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        
        for i in range(len(nums) - 1, 0, -1):
            low, high = 0, i-1
            
            while low < high:
                
                if nums[low] + nums[high] > nums[i]:
                    ans += high - low
                    high -= 1
                    
                else:
                    low += 1
        
        return ans
```
