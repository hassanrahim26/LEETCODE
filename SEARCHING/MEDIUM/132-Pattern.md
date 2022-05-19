## [132 Pattern](https://leetcode.com/problems/132-pattern/)

* **C++**
```cpp
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = INT_MIN;
        stack<int> s;
        
        for(int i = nums.size() - 1; i >= 0; i--){
            if(nums[i] < n)
                return true;
            else
            {
                while(!s.empty() and nums[i] > s.top())
                {
                    n = s.top();
                    s.pop();
                }
            }
            
            s.push(nums[i]);
        }
        
        return false;
    }
};
```

* **Python**
```py
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if(len(nums) < 3):
            return False
        
        n = -math.inf
        s = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < n:
                return True
            
            while s and s[-1] < nums[i]:
                n = s.pop()
            
            s.append(nums[i])
        
        return False
```
