## [Maximum Distance Between a Pair of Values](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/)

* **C++**
```cpp
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int ans = 0, n = nums1.size(), m = nums2.size();
        
        for(int i = 0; i < n; i++)
        {
            int low = i, high = m - 1, j = i;
            
            while(low <= high)
            {
                int mid = low + (high - low)/2;
                
                if(nums2[mid] >= nums1[i])
                {
                    low = mid + 1;
                    j = mid;
                }
                
                else
                    high = mid - 1;
            }
            
            ans = max(ans, j - i);
        }
        
        return ans;
    }
};
```

* **Python**
```py
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans, n, m = 0, len(nums1), len(nums2)
        
        for i in range(0, n):
            low, high, j = i, m - 1, i
            
            while low <= high:
                mid = low + (high - low)//2
                
                if nums2[mid] >= nums1[i]:
                    low = mid + 1
                    j = mid
                else:
                    high = mid - 1
            
            ans = max(ans, j - i)
            
        return ans
```
