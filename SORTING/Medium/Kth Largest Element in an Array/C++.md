[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

* **1**
```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        return nums[n - k];
    }
};
```

* **2**
```cpp
// Using priotiy queue
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for(int i = 1; i < k; i++)
            pq.pop();
        return pq.top();
    }
};
```
