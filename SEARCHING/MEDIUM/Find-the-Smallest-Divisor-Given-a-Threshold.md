## [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

* **C++**
```cpp
class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int low = 1, high = 1e6, mid, sum;
        
        while(low < high){
            mid = low + (high - low)/2;
            sum = 0;
            
            for(int x: nums)
                sum += (x + mid - 1)/mid;
            
            if(sum > threshold)
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
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        
        while low < high:
            mid = low + (high - low)//2
            s = 0
            
            for x in nums:
                s += (x + mid - 1)//mid
                
            if s > threshold:
                low = mid + 1
            else:
                high = mid
        
        return low
```
