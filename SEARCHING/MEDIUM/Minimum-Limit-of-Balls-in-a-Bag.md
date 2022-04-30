## [Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

* **C++**
```cpp
class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int low = 1, high = 1e9;
        
        while(low < high){
            int mid = low + (high - low)/2, count = 0;
            
            for(int x: nums)
                count += (x - 1)/mid;
            
            if(count > maxOperations)
                low = mid + 1;
            else
                high = mid;
        }
        
        return low;
    }
};
```

* **Python**
```py
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        
        while low < high:
            mid = low + (high - low)//2
            count = 0
            
            for x in nums:
                count += (x - 1)//mid
            
            if count > maxOperations:
                low = mid + 1
            else:
                high = mid
        
        return low
```
