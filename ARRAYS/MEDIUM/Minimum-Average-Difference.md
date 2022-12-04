## [Minimum Average Difference](https://leetcode.com/problems/minimum-average-difference/)

* **C++**
```cpp
class Solution {
public:
    int minimumAverageDifference(vector<int>& nums) {
        long tsum = 0, csum = 0;
        int n = nums.size();
        
        for(auto i: nums)
            tsum += i;
        
        int m = INT_MAX, x = 0;
        for(int i = 0; i < n; i++){
            csum += nums[i];
            int avg1 = csum/(i+1);
            if(i == n-1){
                if(avg1 < m)
                    return n-1;
                else
                    break;
            }
            int avg2 = (tsum - csum)/(n-i-1);
            if(abs(avg1 - avg2) < m){
                m = abs(avg1 - avg2);
                x = i;
            }
        }
        return x;
    }
};
```

* **PYTHON**
```py
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        tsum, csum, n = 0, 0, len(nums)
        for i in nums:
            tsum += i
        m, x = float('inf'), 0
        
        for i in range(n):
            avg1, avg2 = 0, 0
            csum += nums[i]
            avg1 = csum//(i+1)
            if(i == n-1):
                if(avg1 < m):
                    return n-1
                else:
                    break
                    
            avg2 = (tsum - csum)//(n-i-1)
            if(abs(avg1 - avg2) < m):
                m = abs(avg1 - avg2)
                x = i
        return x
```
