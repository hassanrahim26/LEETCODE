## [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)

* **C++**
```cpp
class Solution {
public:
    int c;
    
    void solve(vector<int>& nums, int start, int mid, int end)
    {
        int l = start, r = mid + 1;
        while(l <= mid && r <= end)
        {
            if((long)nums[l] > (long)2 * nums[r ])
            {
                c += (mid - l + 1);
                r++;
            }
            else
            {
                l++;
            }
        }
        sort(nums.begin() + start, nums.begin() + end + 1);
        return;
    }
    
    void mergeSort(vector<int>& nums, int start, int end)
    {
        if(start == end)
            return;
        
        int mid = (start + end)/2;
        mergeSort(nums, start, mid);
        mergeSort(nums, mid+1, end);
        
        solve(nums, start, mid, end);
        return;
    }
    
    int reversePairs(vector<int>& nums) 
    {
        if(!nums.size())    
            return 0;
        c = 0;
        mergeSort(nums, 0, nums.size() - 1);
        return c;
    }
};
```
