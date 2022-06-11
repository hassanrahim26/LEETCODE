## [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

* **C++**
```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int i, s1 = 0, s2 = 0, len = 0;
        
        for(i = 0; i < nums.size(); i++){
            s2 += nums[i];
        }
        
        s2 -= x;
        
        if(s2 == 0)
            return nums.size();
        
        i = 0;
        for(int j = 0; j < nums.size(); j++){
            s1 += nums[j];
            
            while(i < nums.size() and s1 > s2)
                s1 -= nums[i++];
            
            if(s1 == s2)
                len = max(len, j - i + 1);
        }
        
        if(!len)
            return -1;
        return nums.size() - len;
    }
};
```
