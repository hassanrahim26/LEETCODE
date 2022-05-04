## [Minimum Absolute Sum Difference](https://leetcode.com/problems/minimum-absolute-sum-difference/)

* **C++**
```cpp
class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        long sum = 0, minSum;
        vector<int> v = nums1;
        int n = v.size();
        
        for(int i = 0; i < n; i++)
            sum += abs(nums1[i] - nums2[i]);
        
        sort(v.begin(), v.end());
        minSum = sum;
        
        for(int i = 0; i < n; i++){
            int diff = abs(nums1[i] - nums2[i]);
            int low = 0, high = n - 1;
            
            while(low < high){
                int mid = low + (high - low)/2;
                
                if(v[mid] > nums2[i])
                    high = mid;
                else
                    low = mid + 1;
                
                diff = min(diff, abs(v[mid] - nums2[i]));
            }
            
            diff = min(diff, abs(nums2[i] - v[low]));
            minSum = min(minSum, sum - abs(nums1[i] - nums2[i]) + diff);
        }
        
        return minSum % 1000000007;
    }
};
```

