## [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

* **C++**
```cpp
class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> st;
        int curr_sum = 0, max_sum = 0, l = 0;
        
        for(int x: nums){
            while(st.find(x) != st.end()){
                curr_sum -= nums[l];
                st.erase(nums[l]);
                l += 1;
            }
            
            curr_sum += x;
            st.insert(x);
            max_sum = max(curr_sum, max_sum);
        }
        
        return max_sum;
    }
};
```

* **Python**
```py
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        st = set()
        curr_sum, max_sum, l = 0, 0, 0
        
        for x in nums:
            while x in st:
                curr_sum -= nums[l]
                st.remove(nums[l])
                l += 1
            curr_sum += x
            st.add(x)
            max_sum = max(curr_sum, max_sum)
            
        return max_sum
```
